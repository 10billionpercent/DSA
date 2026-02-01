// Chocolate AI Backend Canister
import Array "mo:core/Array";
import Int "mo:core/Int";
import Text "mo:core/Text";
import Time "mo:core/Time";
import Map "mo:core/Map";
import Runtime "mo:core/Runtime";
import Iter "mo:core/Iter";
import Principal "mo:core/Principal";
import AccessControl "authorization/access-control";
import MixinAuthorization "authorization/MixinAuthorization";

actor {
  // Initialize the access control system
  let accessControlState = AccessControl.initState();
  include MixinAuthorization(accessControlState);

  // User Profile Type
  public type UserProfile = {
    name : Text;
  };

  // Recipe Type with owner field (internal storage)
  type Recipe = {
    id : Text;
    title : Text;
    description : Text;
    ingredients : [Text];
    steps : [Text];
    tags : [Text];
    timestamp : Int;
    owner : Principal;
  };

  // Recipe Input Type (without owner field - for client submissions)
  public type RecipeInput = {
    id : Text;
    title : Text;
    description : Text;
    ingredients : [Text];
    steps : [Text];
    tags : [Text];
  };

  let recipes = Map.empty<Text, Recipe>();
  let userProfiles = Map.empty<Principal, UserProfile>();

  // User Profile Management Functions
  public query ({ caller }) func getCallerUserProfile() : async ?UserProfile {
    if (not (AccessControl.hasPermission(accessControlState, caller, #user))) {
      Runtime.trap("Unauthorized: Only users can access profiles");
    };
    userProfiles.get(caller);
  };

  public query ({ caller }) func getUserProfile(user : Principal) : async ?UserProfile {
    if (caller != user and not AccessControl.isAdmin(accessControlState, caller)) {
      Runtime.trap("Unauthorized: Can only view your own profile");
    };
    userProfiles.get(user);
  };

  public shared ({ caller }) func saveCallerUserProfile(profile : UserProfile) : async () {
    if (not (AccessControl.hasPermission(accessControlState, caller, #user))) {
      Runtime.trap("Unauthorized: Only users can save profiles");
    };
    userProfiles.add(caller, profile);
  };

  // Recipe Management Functions

  // Public query - accessible to everyone including guests
  public query ({ caller }) func getAllRecipes() : async [Recipe] {
    recipes.values().toArray();
  };

  // Requires user authentication - only logged-in users can save recipes
  public shared ({ caller }) func addRecipe(recipeInput : RecipeInput) : async () {
    if (not (AccessControl.hasPermission(accessControlState, caller, #user))) {
      Runtime.trap("Unauthorized: Only users can save recipes");
    };

    let recipe : Recipe = {
      id = recipeInput.id;
      title = recipeInput.title;
      description = recipeInput.description;
      ingredients = recipeInput.ingredients;
      steps = recipeInput.steps;
      tags = recipeInput.tags;
      timestamp = Time.now();
      owner = caller; // Always set the caller as the owner
    };

    recipes.add(recipe.id, recipe);
  };

  // Requires ownership verification - users can only delete their own recipes
  public shared ({ caller }) func deleteRecipe(id : Text) : async () {
    if (not (AccessControl.hasPermission(accessControlState, caller, #user))) {
      Runtime.trap("Unauthorized: Only users can delete recipes");
    };

    switch (recipes.get(id)) {
      case (null) {
        Runtime.trap("Recipe with ID " # id # " does not exist");
      };
      case (?recipe) {
        // Check ownership - only owner or admin can delete
        if (recipe.owner != caller and not AccessControl.isAdmin(accessControlState, caller)) {
          Runtime.trap("Unauthorized: You can only delete your own recipes");
        };
        recipes.remove(id);
      };
    };
  };

  // Public query - accessible to everyone including guests
  public query ({ caller }) func getRecipeById(id : Text) : async Recipe {
    switch (recipes.get(id)) {
      case (?recipe) { recipe };
      case (null) { Runtime.trap("Recipe not found") };
    };
  };

  // Public query - accessible to everyone including guests
  public query ({ caller }) func getRecipesByTag(tag : Text) : async [Recipe] {
    let filteredRecipes = recipes.values().toArray().filter(
      func(recipe) {
        recipe.tags.find(
          func(t) { if (t == tag) { return true } else { false } }
        ) != null;
      }
    );
    filteredRecipes;
  };

  // Requires ownership verification - users can only update their own recipes
  public shared ({ caller }) func updateRecipe(recipeInput : RecipeInput) : async () {
    if (not (AccessControl.hasPermission(accessControlState, caller, #user))) {
      Runtime.trap("Unauthorized: Only users can update recipes");
    };

    switch (recipes.get(recipeInput.id)) {
      case (null) {
        Runtime.trap("Recipe with ID " # recipeInput.id # " does not exist");
      };
      case (?existingRecipe) {
        // Check ownership - only owner or admin can update
        if (existingRecipe.owner != caller and not AccessControl.isAdmin(accessControlState, caller)) {
          Runtime.trap("Unauthorized: You can only update your own recipes");
        };

        let recipe : Recipe = {
          id = recipeInput.id;
          title = recipeInput.title;
          description = recipeInput.description;
          ingredients = recipeInput.ingredients;
          steps = recipeInput.steps;
          tags = recipeInput.tags;
          timestamp = Time.now();
          owner = existingRecipe.owner; // Preserve original owner
        };

        recipes.add(recipe.id, recipe);
      };
    };
  };
};