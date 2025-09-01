# FastAPI Starter Kit with PostgreSQL and Redis

A reusable FastAPI starter template featuring PostgreSQL database integration, Redis caching, and a clean project structure for building robust RESTful APIs.
## Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **PostgreSQL Integration**: SQLAlchemy ORM with async support
- **Redis Caching**: Performance optimization with Redis caching layer
- **Pydantic Schemas**: Type-safe data validation and serialization
- **Modular Structure**: Clean separation of concerns (models, schemas, CRUD operations)
- **Automatic DB Initialization**: Database tables created automatically on startup
- **Production Ready**: Includes caching, error handling, and proper API documentation
## Project Structure

```
.
├── main.py          # FastAPI application entry point and route definitions
├── database.py      # PostgreSQL database configuration and session management
├── models.py        # SQLAlchemy ORM models
├── schemas.py       # Pydantic schemas for request/response validation
├── crud.py          # Database operations (Create, Read, Update, Delete)
├── redis_cache.py   # Redis caching utilities and client configuration
├── README.md        # This file
└── .gitignore       # Git ignore rules for Python projects
```

## Quick Start
### Prerequisites

- Python 3.8+
- PostgreSQL database
- Redis server

### Installation

1. **Clone or use this template**:
```bash
# Use as template
git clone https://github.com/ParzivalXIII/fastapi-starter-kit
cd https://github.com/ParzivalXIII/fastapi-starter-kit
```

2. **Install dependencies**:
```bash
# Using requirements.txt
pip install -r requirements.txt

# Or manually
pip install fastapi uvicorn sqlalchemy asyncpg redis pydantic
```

3. **Configure environment**:
   - Update database credentials in `database.py`
   - Configure Redis connection in `redis_cache.py` if needed
4. **Run the application**:
```bash
python main.py
```

The API will be available at `http://localhost:8000` with automatic Swagger UI documentation at `http://localhost:8000/docs`

## API Endpoints

- `POST /user/` - Create a new user
- `GET /user/{user_id}` - Get user by ID

1. **Define Model** in `models.py`:
```python
class NewModel(Base):
    __tablename__ = "new_models"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
```

2. **Create Schema** in `schemas.py`:
```python
class NewModelCreate(BaseModel):
    name: str

class NewModelSchema(BaseModel):
    id: int
    name: str
    class Config:
        from_attributes = True
```

3. **Add CRUD Operations** in `crud.py`:
```python
def create_new_model(db: Session, new_model: schemas.NewModelCreate):
    db_model = models.NewModel(name=new_model.name)
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model
```

4. **Add Routes** in `main.py`:
```python
@app.post("/new-model/", response_model=schemas.NewModelSchema)
def create_new_model(new_model: schemas.NewModelCreate, db: Session = Depends(get_db)):
    return crud.create_new_model(db, new_model)
```

### Environment Configuration

For production use, consider moving configuration to environment variables:

```python
# In database.py
import os
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "yourdbname")
# ... etc
```

## API Endpoints

- `POST /user/` - Create a new user
- `GET /user/{user_id}` - Get user by ID

## Development

```bash
# Development with auto-reload
uvicorn main:app --reload

# Production
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Deployment Considerations

- Use environment variables for sensitive configuration
- Consider using Docker for containerization
- Set up proper Redis and PostgreSQL connections for production
- Implement proper error handling and logging
- Add authentication and authorization as needed

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

MIT License - Feel free to use this as a template for your projects!
```
---

## Author

This project was created and is maintained by https://github.com/ParzivalXIII. You can contact me via Twitter [@ParzivalXIII].

If you have any questions, feedback, or would like to contribute, please don't hesitate to reach out!