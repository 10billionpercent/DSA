```mermaid
flowchart LR

    %% ===== CLIENT LAYER ===== %%
    subgraph CLIENT["Client (React Frontend)"]
        C1[Login Page]
        C2[Dashboard]
        C3[Document Upload]
        C4[Document List & Search]
        C5[PDF Viewer (iframe)]
    end

    %% ===== BACKEND LAYER ===== %%
    subgraph BACKEND["Backend (Node.js + Express)"]
        B1[Auth Module (JWT + bcrypt)]
        B2[Document Upload API]
        B3[Document View/Download API]
        B4[Search & Metadata Handler]
        B5[Multer (File Handler)]
        B6[GridFSBucket (Connector)]
    end

    %% ===== DATABASE LAYER ===== %%
    subgraph DATABASE["Database (MongoDB + GridFS)"]
        D1[User Collection]
        D2[Document Metadata Collection]
        D3[GridFS (fs.files)]
        D4[GridFS (fs.chunks)]
    end

    %% === FLOWS === %%
    CLIENT -->|HTTP Requests| BACKEND
    BACKEND -->|Validate Token| B1

    %% Upload Flow
    C3 -->|Upload File| B2 --> B5 -->|File Upload Stream| B6 --> D3
    D3 --> D4

    %% Metadata Flow
    B2 -->|Store Metadata| D2
    B4 -->|Metadata Query| D2

    %% Download/View Flow
    C5 <-->|PDF Stream| B3 <-->|File Stream| B6 <-->|Chunks| D4
```

    %% Login/Auth Flow
    C1 -->|Credentials| B1 -->|User Data| D1
