# 📊 SIMRP - User Flow, Use Case & Architecture Diagrams

Dokumentasi visual untuk user flow, use case, dan arsitektur SIMRP.

---

##  TABLE OF CONTENTS

### User Flow & Use Case
1. [Use Case Diagram](#1-use-case-diagram)
2. [User Flow - Relawan](#2-user-flow---relawan)
3. [User Flow - Submit Report](#3-user-flow---submit-report)
4. [User Flow - Approve Event](#4-user-flow---approve-event)
5. [User Flow - Verify Report](#5-user-flow---verify-report)
6. [Event Lifecycle](#6-event-lifecycle)
7. [State Diagram - Event](#7-state-diagram---event)
8. [State Diagram - Report](#8-state-diagram---report)
9. [Sequence Diagram - Login](#9-sequence-diagram---login)
10. [Sequence Diagram - Submit Report](#10-sequence-diagram---submit-report)

### Architecture Diagrams
11. [System Overview](#11-system-overview)
12. [Backend Architecture](#12-backend-architecture)
13. [Frontend Architecture](#13-frontend-architecture)
14. [Deployment Architecture](#14-deployment-architecture)
15. [Data Flow Architecture](#15-data-flow-architecture)
16. [Security Architecture](#16-security-architecture)
17. [Database Schema](#17-database-schema)

### Documentation
18. [Activity Matrix](#18-activity-matrix)
19. [Actor Definitions](#19-actor-definitions)

---

## 1. USE CASE DIAGRAM

```mermaid
flowchart LR
    subgraph Actors
        U[👤 Relawan]
        K[👤 KSH]
        M1[👤 Moderator T1]
        M2[👤 Moderator T2]
        A[👤 Administrator]
    end
    
    subgraph UseCases
        UC1[UC-01 Register]
        UC2[UC-02 Login]
        UC3[UC-03 Browse Events]
        UC4[UC-04 Join Event]
        UC5[UC-05 Submit Report]
        UC6[UC-06 Mark Event Completed]
        UC7[UC-07 Create Event]
        UC8[UC-08 Approve Event]
        UC9[UC-09 Verify Report]
        UC10[UC-10 Manage Users]
        UC11[UC-11 View Leaderboard]
        UC12[UC-12 View Dashboard]
    end
    
    U --> UC1
    U --> UC2
    U --> UC3
    U --> UC4
    U --> UC5
    U --> UC11
    U --> UC12
    
    K --> UC2
    K --> UC3
    K --> UC4
    K --> UC5
    K --> UC6
    K --> UC11
    K --> UC12
    
    M1 --> UC2
    M1 --> UC7
    M1 --> UC12
    
    M2 --> UC2
    M2 --> UC8
    M2 --> UC9
    M2 --> UC12
    
    A --> UC2
    A --> UC8
    A --> UC9
    A --> UC10
    A --> UC12
```

---

## 2. USER FLOW - RELAWAN

```mermaid
flowchart TD
    A([Start]) --> B[Landing Page]
    B --> C{Already Logged In?}
    C -->|No| D[Login Page]
    C -->|Yes| E[Dashboard]
    
    D --> F{New User?}
    F -->|Yes| G[Register Page]
    F -->|No| H[Enter Email & Password]
    
    G --> I[Fill: Name, Email, Password]
    I --> J[Enter Postal Code]
    J --> K{Valid Postal Code?}
    K -->|No| L[❌ Show Error]
    K -->|Yes| M[Auto-fill Kecamatan/Kelurahan]
    M --> N[Submit Registration]
    N --> O{Success?}
    O -->|No| L
    O -->|Yes| P[Auto Login]
    
    H --> Q{Valid Credentials?}
    Q -->|No| R[❌ Show Error]
    Q -->|Yes| P
    
    P --> E
    
    E --> S{Select Menu}
    S --> T[Home Tab]
    S --> U[Events Tab]
    S --> V[Profile Tab]
    S --> W[More Tab]
    
    T --> T1[View Level Progress]
    T --> T2[View Badges]
    T --> T3[View Recent Reports]
    
    U --> U1[Browse Events]
    U1 --> U2{Filter by Pilar?}
    U2 -->|Yes| U3[Select Pilar 1-4]
    U2 -->|No| U4[View All Events]
    U3 --> U4
    U4 --> U5{Select Event}
    U5 -->|Yes| U6[View Event Details]
    U6 --> U7{Join Event?}
    U7 -->|Yes| U8{Quota Available?}
    U8 -->|No| U9[Quota Full]
    U8 -->|Yes| U10[Register as Participant]
    U10 --> U11[✓ Success]
    
    V --> V1[View Profile]
    V1 --> V2[Edit Profile]
    V1 --> V3[View Statistics]
    
    W --> W1[Collaboration]
    W --> W2[About]
    W --> W3[FAQ]
    W --> W4[Logout]
    
    L --> J
    R --> D
    U9 --> U4
    W4 --> A
```

---

## 3. USER FLOW - SUBMIT REPORT

```mermaid
flowchart TD
    A([Event Completed]) --> B[Click Buat Laporan]
    B --> C[Step 1: Photo Upload]
    
    C --> C1[Select Photo Source]
    C1 --> C2[Camera]
    C1 --> C3[Gallery]
    
    C2 --> D[Take Photo]
    C3 --> D[Select Photo]
    
    D --> E[Photo Preview]
    E --> F[Auto-capture GPS Location]
    F --> G[Enter Participants Count]
    G --> H{Valid Count?}
    H -->|No| I[❌ Show Error]
    H -->|Yes| J[Click Lanjut]
    
    J --> K[Step 2: Outcome Tags]
    K --> L[Select from Predefined Tags]
    L --> M{Tag Count <= 20?}
    M -->|No| N[⚠️ Max 20 Tags]
    M -->|Yes| O[Click Kirim Laporan]
    
    O --> P{Submission Success?}
    P -->|No| Q[❌ Show Error]
    P -->|Yes| R[✓ Success]
    
    R --> S[Status: Pending]
    S --> T[Update: Reported]
    T --> U([Complete])
    
    I --> G
    N --> L
    Q --> C
```

---

## 4. USER FLOW - APPROVE EVENT

```mermaid
flowchart TD
    A([Moderator T2 Login]) --> B[Dashboard]
    B --> C[Event Management]
    C --> D[View Pending Drafts]
    
    D --> E{Drafts Available?}
    E -->|No| F[No Pending Drafts]
    E -->|Yes| G[Select Draft]
    
    G --> H[View Draft Details]
    H --> I{Check Jurisdiction}
    
    I -->|Invalid| J[❌ Wrong Jurisdiction]
    I -->|Valid| K[Review Complete]
    
    K --> L{Approve?}
    L -->|Yes| M[Click Approve]
    L -->|No| N[Click Reject]
    
    M --> O[Status: Published]
    N --> P[Status: Draft]
    
    O --> Q[Notify Creator]
    P --> Q
    
    Q --> R[✓ Success]
    R --> S([Complete])
    
    F --> S
    J --> C
```

---

## 5. USER FLOW - VERIFY REPORT

```mermaid
flowchart TD
    A([Moderator Login]) --> B[Report Verification]
    B --> C[View Pending Reports]
    
    C --> D{Reports Available?}
    D -->|No| E[No Pending Reports]
    D -->|Yes| F[Select Report]
    
    F --> G[View Report Details]
    G --> H{Verify?}
    
    H -->|Yes| I[Click Approve]
    H -->|No| J[Click Reject]
    
    I --> K[Calculate XP]
    K --> L[Final XP]
    L --> M[Award XP]
    M --> N[Award Points]
    N --> O[Status: Verified]
    
    J --> Q[Status: Rejected]
    
    O --> R[Notify User]
    Q --> R
    
    R --> S[✓ Success]
    S --> T([Complete])
    
    E --> T
```

---

## 6. EVENT LIFECYCLE

```mermaid
flowchart TD
    A([Start]) --> B[Moderator T1: Create Event]
    B --> C[Fill Event Form]
    C --> D[Select Scope]
    D --> E[Submit Draft]
    
    E --> F[Status: Draft]
    F --> G[Moderator T2: Review]
    
    G --> H{Check Jurisdiction}
    H -->|Invalid| I[❌ Cannot Approve]
    H -->|Valid| J{Approve?}
    
    J -->|No| K[Reject]
    K --> F
    
    J -->|Yes| L[Status: Published]
    L --> M[Visible to Public]
    
    M --> N[Relawan: Browse]
    N --> O[Relawan: Join]
    O --> P[Participants Registered]
    
    P --> Q[Event Day]
    Q --> R[Event Conducted]
    
    R --> S[KSH: Mark Complete]
    S --> T[Add Summary]
    T --> U[Status: Completed]
    
    U --> V[7-Day Report Window]
    V --> W[Relawan: Submit Report]
    
    W --> X[Moderator: Verify]
    X --> Y{Verify?}
    
    Y -->|No| Z[Rejected]
    Z --> Z1[Can Resubmit]
    Z1 --> W
    
    Y -->|Yes| AA[Calculate XP]
    AA --> AB[Award XP]
    AB --> AC[Award Points]
    AC --> AD[Verified]
    
    AD --> AE[Update Leaderboard]
    AE --> AF([Complete])
    
    I --> F
```

---

## 7. STATE DIAGRAM - EVENT

```mermaid
stateDiagram-v2
    [*] --> Draft
    
    Draft --> PendingApproval: Submit Draft
    PendingApproval --> Draft: Rejected
    PendingApproval --> Published: Approved
    
    Published --> Completed: KSH Marks Complete
    Completed --> Reported: Report Submitted
    Reported --> Completed: More Reports
    Reported --> Verified: Report Verified
    Verified --> [*]
    
    note right of Draft
        Initial state
        Editable by creator
    end note
    
    note right of Published
        Visible to public
        Users can join
    end note
    
    note right of Completed
        Event finished
        Reports accepted
    end note
    
    note right of Verified
        XP awarded
        Points given
    end note
```

---

## 8. STATE DIAGRAM - REPORT

```mermaid
stateDiagram-v2
    [*] --> Pending: User Submits
    
    Pending --> Verified: Moderator Approves
    Pending --> Rejected: Moderator Rejects
    
    Verified --> [*]: Complete
    Rejected --> Pending: User Resubmits
    Rejected --> [*]: Final
    
    note right of Pending
        Awaiting verification
    end note
    
    note right of Verified
        XP awarded
        +5 points to user
    end note
    
    note right of Rejected
        Can resubmit
    end note
```

---

## 9. SEQUENCE DIAGRAM - LOGIN

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant Frontend
    participant API
    participant AuthService
    participant Database
    
    User->>Frontend: Enter email & password
    User->>Frontend: Click Login
    
    Frontend->>API: POST /auth/login
    API->>AuthService: login(email, password)
    AuthService->>Database: SELECT * FROM users
    Database-->>AuthService: User record
    
    alt User not found
        AuthService-->>API: Error
        API-->>Frontend: 401
    else Password invalid
        AuthService-->>API: Error
        API-->>Frontend: 401
    else Success
        AuthService->>Database: INSERT session
        Database-->>AuthService: Token
        AuthService-->>API: {token, user}
        API-->>Frontend: 200 OK
    end
```

---

## 10. SEQUENCE DIAGRAM - SUBMIT REPORT

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant Frontend
    participant API
    participant ReportService
    participant Database
    
    User->>Frontend: Click Kirim Laporan
    Frontend->>API: POST /reports
    API->>ReportService: createReport(data)
    ReportService->>Database: INSERT report
    Database-->>ReportService: Report ID
    ReportService->>Database: UPDATE participation
    ReportService-->>API: {reportId}
    API-->>Frontend: 200 OK
    Frontend-->>User: Success toast
```

---

## 11. SYSTEM OVERVIEW

```mermaid
flowchart TB
    subgraph SIMRP["SIMRP System"]
        Frontend[browser Frontend]
        Backend[server Backend API]
        Database[(database SQLite DB)]
        Storage[disk File Storage]
    end
    
    Frontend --> Backend
    Backend --> Database
    Backend --> Storage
    
    style SIMRP fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style Frontend fill:#4CAF50,color:#fff
    style Backend fill:#2196F3,color:#fff
    style Database fill:#FF9800,color:#fff
    style Storage fill:#9C27B0,color:#fff
```

---

## 12. BACKEND ARCHITECTURE

```mermaid
flowchart TB
    %% ROUTES LAYER
    subgraph Routes["Routes Layer"]
        auth_route[Auth Route]
        event_route[Event Route]
        report_route[Report Route]
        admin_route[Admin Route]
    end
    
    %% SERVICES LAYER
    subgraph Services["Services Layer"]
        auth_svc[Auth Service]
        event_svc[Event Service]
        report_svc[Report Service]
        admin_svc[Admin Service]
    end
    
    %% REPOSITORIES LAYER
    subgraph Repositories["Repository Layer"]
        user_repo[User Repository]
        event_repo[Event Repository]
        report_repo[Report Repository]
    end
    
    %% CORE LAYER
    subgraph Core["Core Layer"]
        db_core[Database]
        security_core[Security]
        config_core[Config]
    end
    
    %% CONNECTIONS
    auth_route --> auth_svc
    event_route --> event_svc
    report_route --> report_svc
    admin_route --> admin_svc
    
    auth_svc --> user_repo
    event_svc --> event_repo
    report_svc --> report_repo
    
    user_repo --> db_core
    event_repo --> db_core
    report_repo --> db_core
    
    auth_svc --> security_core
    db_core --> config_core
    
    style Routes fill:#e3f2fd,stroke:#1976d2
    style Services fill:#fff3e0,stroke:#f57c00
    style Repositories fill:#f3e5f5,stroke:#7b1fa2
    style Core fill:#e8f5e9,stroke:#388e3c
```

---

## 13. FRONTEND ARCHITECTURE

```mermaid
flowchart TB
    %% PAGES
    subgraph Pages["Pages"]
        landing[Landing Page]
        login[Login Page]
        dashboard[Dashboard Page]
        admin[Admin Page]
    end
    
    %% COMPONENTS
    subgraph Components["Components"]
        shared[Shared Components]
        ui[UI Kit]
        features[Feature Components]
    end
    
    %% SERVICES
    subgraph Services["Services"]
        api[API Client]
        auth[Auth Service]
    end
    
    %% STATE
    subgraph State["State Management"]
        user[User State]
        session[Session State]
    end
    
    %% CONNECTIONS
    landing --> Components
    login --> Components
    dashboard --> Components
    admin --> Components
    
    Components --> State
    Pages --> Services
    Services --> api
    
    style Pages fill:#e3f2fd,stroke:#1976d2
    style Components fill:#fff3e0,stroke:#f57c00
    style Services fill:#f3e5f5,stroke:#7b1fa2
    style State fill:#e8f5e9,stroke:#388e3c
```

---

## 14. DEPLOYMENT ARCHITECTURE

```mermaid
flowchart TB
    %% CLIENTS
    subgraph Clients["Client Devices"]
        desktop[Desktop Browser]
        mobile[Mobile Browser]
        tablet[Tablet Browser]
    end
    
    %% SERVER
    subgraph Server["Server Infrastructure"]
        nginx[nginx Reverse Proxy]
        python[Python HTTP Server]
        static[Static Files]
    end
    
    %% STORAGE
    subgraph Storage["Storage"]
        sqlite[(SQLite Database)]
        backups[Backup Files]
        logs[Log Files]
    end
    
    %% EXTERNAL
    subgraph External["External Services"]
        ssl[SSL Certificate]
        monitoring[Monitoring]
    end
    
    %% CONNECTIONS
    desktop --> nginx
    mobile --> nginx
    tablet --> nginx
    
    nginx --> python
    nginx --> static
    
    python --> sqlite
    sqlite --> backups
    python --> logs
    
    nginx -.-> ssl
    python -.-> monitoring
    
    style Clients fill:#e3f2fd,stroke:#1976d2
    style Server fill:#fff3e0,stroke:#f57c00
    style Storage fill:#f3e5f5,stroke:#7b1fa2
    style External fill:#e8f5e9,stroke:#388e3c
```

---

## 15. DATA FLOW ARCHITECTURE

```mermaid
flowchart TB
    %% INPUT
    subgraph Input["Input Layer"]
        user_input[User Input]
        api_input[API Input]
    end
    
    %% PROCESSING
    subgraph Processing["Processing Layer"]
        validation[Validation]
        auth[Authentication]
        business[Business Logic]
    end
    
    %% STORAGE
    subgraph DataStores["Data Stores"]
        users_db[(Users DB)]
        events_db[(Events DB)]
        reports_db[(Reports DB)]
        sessions_db[(Sessions DB)]
    end
    
    %% OUTPUT
    subgraph Output["Output Layer"]
        dashboard[Dashboard]
        api_response[API Response]
        reports[Reports]
    end
    
    %% CONNECTIONS
    user_input --> validation
    api_input --> validation
    
    validation --> auth
    auth --> business
    
    business --> users_db
    business --> events_db
    business --> reports_db
    business --> sessions_db
    
    users_db --> dashboard
    events_db --> api_response
    reports_db --> reports
    
    style Input fill:#e3f2fd,stroke:#1976d2
    style Processing fill:#fff3e0,stroke:#f57c00
    style DataStores fill:#f3e5f5,stroke:#7b1fa2
    style Output fill:#e8f5e9,stroke:#388e3c
```

---

## 16. SECURITY ARCHITECTURE

```mermaid
flowchart TB
    %% PERIMETER
    subgraph Perimeter["Security Perimeter"]
        firewall[Firewall]
        ratelimit[Rate Limiter]
        cors[CORS]
    end
    
    %% AUTH
    subgraph Auth["Authentication"]
        login[Login]
        session[Session Management]
        token[Token Generation]
    end
    
    %% CRYPTO
    subgraph Crypto["Encryption"]
        pbkdf2[PBKDF2 Hashing]
        https[HTTPS/TLS]
        csp[CSP Headers]
    end
    
    %% AUDIT
    subgraph Audit["Audit Trail"]
        logs[Audit Logs]
        monitoring[Monitoring]
    end
    
    %% CONNECTIONS
    firewall --> ratelimit
    ratelimit --> cors
    cors --> login
    login --> session
    session --> token
    
    token --> pbkdf2
    pbkdf2 --> https
    https --> csp
    
    logs --> monitoring
    firewall -.-> logs
    
    style Perimeter fill:#ffebee,stroke:#c62828
    style Auth fill:#fff3e0,stroke:#f57c00
    style Crypto fill:#e8f5e9,stroke:#388e3c
    style Audit fill:#f3e5f5,stroke:#7b1fa2
```

---

## 17. DATABASE SCHEMA

```mermaid
flowchart TB
    %% USERS
    subgraph Users["Users Schema"]
        users_tbl[users]
        sessions_tbl[sessions]
        roles_tbl[roles]
    end
    
    %% EVENTS
    subgraph Events["Events Schema"]
        events_tbl[events]
        participation_tbl[event_participation]
        reports_tbl[event_reports]
    end
    
    %% GEOGRAPHY
    subgraph Geography["Geography Schema"]
        kecamatan_tbl[kecamatan]
        kelurahan_tbl[kelurahan]
        postal_tbl[postal_codes]
    end
    
    %% XP
    subgraph XP["XP System"]
        xp_kelurahan[xp_kelurahan]
        xp_pillar[xp_pillar]
    end
    
    %% CONNECTIONS
    users_tbl --> participation_tbl
    users_tbl --> reports_tbl
    users_tbl --> sessions_tbl
    
    events_tbl --> participation_tbl
    events_tbl --> reports_tbl
    
    kelurahan_tbl --> kecamatan_tbl
    kelurahan_tbl --> postal_tbl
    kelurahan_tbl --> xp_kelurahan
    
    xp_kelurahan --> xp_pillar
    
    style Users fill:#e3f2fd,stroke:#1976d2
    style Events fill:#fff3e0,stroke:#f57c00
    style Geography fill:#f3e5f5,stroke:#7b1fa2
    style XP fill:#e8f5e9,stroke:#388e3c
```

---

## 18. ACTIVITY MATRIX

| Use Case | Relawan | KSH | Mod T1 | Mod T2 | Mod T3 | Admin |
|----------|:-------:|:---:|:------:|:------:|:------:|:-----:|
| UC-01 Register | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| UC-02 Login | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| UC-03 Browse Events | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| UC-04 Join Event | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| UC-05 Submit Report | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| UC-06 Mark Event Completed | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| UC-07 Create Event | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ |
| UC-08 Approve Event | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| UC-09 Verify Report | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| UC-10 Manage Users | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| UC-11 View Leaderboard | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| UC-12 View Dashboard | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| UC-13 Review Collaboration Request | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |

**Legend:** ✅ = Can perform, ❌ = Cannot perform

---

## 19. ACTOR DEFINITIONS

| Actor | Role Code | Description | Key Responsibilities | Database Fields |
|-------|-----------|-------------|---------------------|-----------------|
| **Relawan** | `user` | Registered volunteer | Join events, submit reports, earn points & badges | `role_code='user'`, `is_ksh=0` |
| **KSH** | `ksh` | Ketua Suku Kampung (Verified Community Partner) | All Relawan + Create events, Mark events complete | `role_code='ksh'`, `is_ksh=1` |
| **Moderator T1** | `moderator_t1` | ASN (Civil Servant) | Create event drafts for review | `role_code='moderator_t1'`, `moderator_tier=1` |
| **Moderator T2** | `moderator_t2` | Lurah/Camat (Village/District Head) | Approve events, Verify reports (geographic jurisdiction via `tier2_badge`: lurah/camat) | `role_code='moderator_t2'`, `moderator_tier=2`, `tier2_badge='lurah' or 'camat'` |
| **Moderator T3** | `moderator_t3` | Senior Moderator (City-level) | Review city-scale collaboration requests, External partner approvals (mitra/kontributor kota) | `role_code='moderator_t3'`, `moderator_tier=3` |
| **Administrator** | `admin` | System Admin | Full access - manage users, moderators, events, system settings, anti-fraud tools | `role_code='admin'` |

### Persona Details:

#### 👤 Relawan (Volunteer)
- **Registration**: Name, Email, Password, Postal Code (auto-fills Kecamatan/Kelurahan)
- **Capabilities**: Browse events, join events, submit reports with photos, view leaderboard
- **Progression**: 7 levels (Pendatang Baru → Legend Kampung)
- **Demo Accounts**: `relawan.demo@simrp.app`, `relawan2.demo@simrp.app`, `relawan3.demo@simrp.app` (password: `password123`)

#### 🏘️ KSH (Ketua Suku Kampung)
- **Role**: Community leader with verified status
- **Capabilities**: All Relawan + Create events, Mark events as complete
- **Badge**: KSH Verified badge in UI
- **Demo Account**: `ksh.demo@simrp.app` / `password123`

#### 🛡️ Moderator Tier 1 (ASN)
- **Role**: Civil servant who creates event drafts
- **Capabilities**: Create events, Submit drafts for approval
- **Scope**: Event creator only, cannot approve
- **Demo Account**: `moderator1.demo@simrp.app` / `password123`

#### 🛡️ Moderator Tier 2 (Lurah/Camat)
- **Role**: Village or district head with geographic jurisdiction
- **Badge System**: `tier2_badge` field determines scope - 'lurah' (village) or 'camat' (district)
- **Capabilities**: Approve/reject events, Verify reports, Award XP
- **Jurisdiction**: Can only approve events within their geographic area
- **Demo Accounts**: 
  - Lurah: `moderator2.demo@simrp.app` / `password123`
  - Camat: `moderator2.camat@simrp.app` / `password123`

#### 🛡️ Moderator Tier 3 (Senior Moderator)
- **Role**: City-level coordinator for external collaborations
- **Capabilities**: Review collaboration requests from city-scale contributors (mitra/kontributor kota), Approve events, Verify reports
- **Scope**: Handles `collaboration_requests` with `contribution_scope='kota'`
- **Use Case**: External partners wanting to contribute at city level get routed here
- **Demo Account**: `moderator3.demo@simrp.app` / `password123`

#### ⚙️ Administrator
- **Role**: System superuser with full control
- **Capabilities**: Manage users, Assign moderators, Adjust points/badges/levels (temporary or permanent), View audit logs, God Mode (POV switching)
- **Anti-Fraud Tools**: Temporary adjustments (24h expiry), Audit trail tracking
- **Demo Account**: Access via `/admin` portal - Username: `admin`, Password: auto-generated (check console on first run)

---

## 20. DATABASE SCHEMA ALIGNMENT

All user flows and personas are fully aligned with the SQLite database schema:

### Core Tables:
- **`users`**: Stores all user accounts with `role_code`, `is_ksh`, `moderator_tier`, `tier2_badge` fields
- **`events`**: Community events with geographic scope (`kecamatan_id`, `kelurahan_id`, `scope_type`)
- **`event_participation`**: User-event registrations with status tracking
- **`event_reports`**: Post-event reports with verification workflow
- **`collaboration_requests`**: External partner requests (handled by Mod T3/Admin)
- **`sessions`**: Auth session management
- **`temporary_adjustments`**: Admin temporary point/badge/role adjustments (24h expiry)
- **`audit_logs`**: Complete audit trail for all admin actions
- **`xp_kelurahan`** & **`xp_pillar`**: Aggregated XP tracking per area and pillar

### Geographic Hierarchy:
- **`kecamatan`** (31 districts in Surabaya)
- **`kelurahan`** (154 sub-villages, FK to kecamatan)
- **`postal_codes`** (200+ postal codes)
- **`kampung_mapping`** (many-to-many: kelurahan ↔ postal_codes)

### Role Validation:
All roles validated against `server/core/config.py`:
```python
VALID_ROLE_CODES = {"user", "ksh", "moderator_t1", "moderator_t2", "moderator_t3", "admin"}
VALID_TIER2_BADGES = {"lurah", "camat"}
```

---

## 📚 REFERENCES

- **Mermaid Flowchart**: https://mermaid.js.org/syntax/flowchart.html
- **Sequence Diagram**: https://mermaid.js.org/syntax/sequenceDiagram.html
- **State Diagram**: https://mermaid.js.org/syntax/stateDiagram.html
- **Project Architecture**: `docs/architecture/ARCHITECTURE.md`

---

**© 2025 Dinas Komunikasi dan Informatika Kota Surabaya**
