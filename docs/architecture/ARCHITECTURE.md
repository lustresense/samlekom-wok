# SIMRP Architecture Documentation

## 📐 Professional Layered Architecture

**Version**: 2.0.0  
**Last Updated**: April 2026  
**Author**: Diskominfo Surabaya

---

## 🏗️ Architecture Overview

SIMRP menggunakan **Layered Architecture** dengan separation of concerns yang jelas untuk maintainability, testability, dan scalability.

```
┌─────────────────────────────────────────────────────────────┐
│                      PRESENTATION LAYER                      │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  Frontend (React + TypeScript + Vite)               │    │
│  │  - Pages                                            │    │
│  │  - Components                                       │    │
│  │  - Hooks                                            │    │
│  │  - Contexts                                         │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                       APPLICATION LAYER                      │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  HTTP Routes (backend/routes/)                      │    │
│  │  - Auth Routes                                      │    │
│  │  - Event Routes                                     │    │
│  │  - Report Routes                                    │    │
│  │  - Admin Routes                                     │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                       BUSINESS LOGIC LAYER                   │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  Services (backend/services/)                       │    │
│  │  - AuthService                                      │    │
│  │  - EventService                                     │    │
│  │  - ReportService                                    │    │
│  │  - AdminService                                     │    │
│  │  - GeographicService                                │    │
│  │  - CollaborationService                             │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                       DATA ACCESS LAYER                      │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  Repositories (backend/repositories/)               │    │
│  │  - UserRepository                                   │    │
│  │  - EventRepository                                  │    │
│  │  - ReportRepository                                 │    │
│  │  - GeographicRepository                             │    │
│  │  - XPRepository                                     │    │
│  │  - SessionRepository                                │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                       CORE LAYER                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  Core Utilities (backend/core/)                     │    │
│  │  - Database Manager                                 │    │
│  │  - Security (hashing, tokens)                       │    │
│  │  - Logging                                          │    │
│  └─────────────────────────────────────────────────────┘    │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  Configuration (backend/config/)                    │    │
│  │  - Environment Variables                            │    │
│  │  - Application Settings                             │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                       DATABASE                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  SQLite                                             │    │
│  │  - Users                                            │    │
│  │  - Events                                           │    │
│  │  - Reports                                          │    │
│  │  - Geographic Data                                  │    │
│  │  - Sessions                                         │    │
│  │  - XP Tracking                                      │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 Directory Structure

```
figmasimrp/
├── backend/                          # Backend application
│   ├── config/                       # Configuration layer
│   │   ├── __init__.py
│   │   ├── settings.py              # Environment variables & settings
│   │   └── logging_config.py        # Logging configuration
│   │
│   ├── core/                         # Core utilities
│   │   ├── __init__.py
│   │   ├── database.py              # Database connection manager
│   │   └── security.py              # Security utilities
│   │
│   ├── models/                       # Data models
│   │   ├── __init__.py
│   │   └── models.py                # Data classes
│   │
│   ├── repositories/                 # Data access layer
│   │   ├── __init__.py
│   │   ├── base_repository.py       # Base repository class
│   │   ├── user_repository.py
│   │   ├── session_repository.py
│   │   ├── event_repository.py
│   │   ├── report_repository.py
│   │   ├── participation_repository.py
│   │   ├── geographic_repository.py
│   │   ├── xp_repository.py
│   │   └── collaboration_repository.py
│   │
│   ├── services/                     # Business logic layer
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── event_service.py
│   │   ├── report_service.py
│   │   ├── admin_service.py
│   │   ├── geographic_service.py
│   │   └── collaboration_service.py
│   │
│   ├── routes/                       # HTTP routes
│   │   ├── __init__.py
│   │   ├── base_handler.py          # Base HTTP handler
│   │   ├── auth_routes.py
│   │   └── health_routes.py
│   │
│   ├── middleware/                   # Middleware
│   │   ├── __init__.py
│   │   ├── rate_limiter.py
│   │   ├── cors.py
│   │   └── security_headers.py
│   │
│   ├── utils/                        # Utilities
│   │   └── __init__.py
│   │
│   ├── server.py                     # Main entry point
│   └── __init__.py
│
├── frontend/                         # Frontend application
│   └── src/
│       ├── config/                   # Frontend configuration
│       ├── components/               # React components
│       │   ├── shared/              # Shared components
│       │   └── features/            # Feature-specific components
│       ├── pages/                    # Page components
│       │   ├── auth/
│       │   ├── dashboard/
│       │   └── public/
│       ├── services/                 # API services
│       ├── hooks/                    # Custom React hooks
│       ├── contexts/                 # React contexts
│       ├── lib/                      # Utility libraries
│       ├── data/                     # Static data
│       ├── styles/                   # Styles
│       ├── types/                    # TypeScript types
│       ├── app/                      # Main app
│       └── main.tsx                  # Entry point
│
├── database/                         # Database files
│   ├── runtime/                     # Runtime database
│   └── backups/                     # Database backups
│
├── docs/                            # Documentation
│   ├── architecture/                # Architecture docs
│   ├── security/                    # Security documentation
│   ├── guides/                      # User guides
│   └── status/                      # Implementation status
│
├── scripts/                         # Build/deployment scripts
├── dist/                            # Build output
└── package.json                     # Dependencies
```

---

## 🔄 Request Flow Example

### User Login Flow

```
1. User submits login form
   │
   ▼
2. Frontend: LoginPage.tsx
   │
   ▼
3. Frontend: api.post('/auth/login', {email, password})
   │
   ▼
4. Backend: SIMRPHTTPHandler.do_POST()
   │
   ▼
5. Backend: AuthRoutes.register_routes()
   │
   ▼
6. Backend: AuthRoutes._handle_login()
   │
   ▼
7. Backend: AuthService.login()
   │
   ├── Validate email format
   ├── Find user (UserRepository)
   ├── Verify password (Security)
   └── Create session (SessionRepository)
   │
   ▼
8. Backend: Return {token, user}
   │
   ▼
9. Frontend: Store token, update state
   │
   ▼
10. Navigate to dashboard
```

---

## 🎯 Design Principles

### 1. **Separation of Concerns**
- Each layer has a single responsibility
- Changes in one layer don't affect others

### 2. **Dependency Inversion**
- High-level modules don't depend on low-level modules
- Both depend on abstractions (interfaces/abstract classes)

### 3. **Single Responsibility**
- Each class/module has one reason to change
- Small, focused components

### 4. **DRY (Don't Repeat Yourself)**
- Common functionality in base classes
- Shared utilities in core layer

### 5. **Security by Design**
- Input validation at all layers
- Authentication/authorization middleware
- Rate limiting
- Security headers

---

## 🔐 Security Architecture

### Authentication Flow
```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Frontend   │────▶│    Routes    │────▶│   Services   │
└──────────────┘     └──────────────┘     └──────────────┘
                            │                    │
                            ▼                    ▼
                     ┌──────────────┐     ┌──────────────┐
                     │  Middleware  │     │ Repositories │
                     └──────────────┘     └──────────────┘
                            │                    │
                            ▼                    ▼
                     ┌──────────────┐     ┌──────────────┐
                     │    Core      │────▶│  Database    │
                     └──────────────┘     └──────────────┘
```

### Security Layers:
1. **Network**: CORS, HTTPS
2. **Application**: Rate limiting, input validation
3. **Authentication**: PBKDF2 hashing, session tokens
4. **Authorization**: Role-based access control
5. **Data**: SQL injection prevention (parameterized queries)

---

## 📊 Database Schema

### Core Tables:
- **users**: User accounts and profiles
- **sessions**: Active user sessions
- **events**: Community events
- **event_participation**: User-event relationships
- **event_reports**: Activity reports
- **kecamatan**: Districts
- **kelurahan**: Villages
- **postal_codes**: Postal codes
- **kampung_mapping**: Kelurahan-postal code mapping
- **xp_kelurahan**: Village XP tracking
- **xp_pillar**: XP per pillar
- **collaboration_requests**: External collaboration
- **temporary_adjustments**: Temporary point/badge adjustments
- **audit_logs**: System audit trail

---

## 🧪 Testing Strategy

### Unit Tests
- Test individual functions/methods
- Mock dependencies
- Focus on business logic (services)

### Integration Tests
- Test layer interactions
- Database operations
- API endpoints

### E2E Tests
- Full user flows
- Frontend + backend integration

---

## 🚀 Deployment Architecture

```
┌─────────────────────────────────────────┐
│  Load Balancer / Reverse Proxy (nginx)  │
│  - SSL/TLS Termination                  │
│  - Rate Limiting                        │
│  - Static File Serving                  │
└─────────────────────────────────────────┘
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
┌──────────────┐        ┌──────────────┐
│  Frontend    │        │   Backend    │
│  (Vite)      │        │   (Python)   │
│  Port 5173   │        │   Port 8000  │
└──────────────┘        └──────────────┘
        │                       │
        └───────────┬───────────┘
                    ▼
           ┌──────────────┐
           │   SQLite     │
           │  Database    │
           └──────────────┘
```

---

## 📈 Scalability Considerations

### Current (SQLite):
- Suitable for development and small production deployments
- Single-file database, easy backup
- Limited concurrency

### Future (PostgreSQL):
```python
# Migration path:
# 1. Replace database.py connection logic
# 2. Update repository queries (minimal changes)
# 3. Keep service layer unchanged
# 4. Keep routes unchanged
```

### Horizontal Scaling:
- Stateless application design
- Session storage can be moved to Redis
- Load balancer for multiple instances

---

## 🛠️ Development Guidelines

### Adding New Features:

1. **Define Models** (`backend/models/models.py`)
   ```python
   @dataclass
   class NewEntity:
       id: str
       name: str
       # ...
   ```

2. **Create Repository** (`backend/repositories/new_repository.py`)
   ```python
   class NewRepository(BaseRepository[NewEntity]):
       # CRUD operations
   ```

3. **Create Service** (`backend/services/new_service.py`)
   ```python
   class NewService:
       # Business logic
   ```

4. **Create Routes** (`backend/routes/new_routes.py`)
   ```python
   class NewRoutes:
       # HTTP handlers
   ```

5. **Register Routes** (in `backend/server.py`)
   ```python
   if NewRoutes.register_routes(self, path, method):
       return True
   ```

### Code Style:
- Type hints for all functions
- Docstrings for all public methods
- Consistent naming conventions
- Error handling at all layers

---

## 📚 References

- **Clean Architecture** by Robert C. Martin
- **Domain-Driven Design** by Eric Evans
- **OWASP Security Guidelines**
- **Python Best Practices** (PEP 8, PEP 484)

---

**© 2025 Dinas Komunikasi dan Informatika Kota Surabaya**
