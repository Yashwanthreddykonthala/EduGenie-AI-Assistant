import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)  # Hashed password
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    queries = relationship("UserQuery", back_populates="user", cascade="all, delete-orphan")


class UserQuery(Base):
    __tablename__ = "user_queries"

    query_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    query_type = Column(String, nullable=False)  # QnA, Explanation, Quiz, Summary, Recommendation
    query_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="queries")
    ai_response = relationship("AIResponse", back_populates="query", uselist=False, cascade="all, delete-orphan")
    quizzes = relationship("Quiz", back_populates="query", cascade="all, delete-orphan")
    summaries = relationship("Summary", back_populates="query", cascade="all, delete-orphan")
    learning_paths = relationship("LearningPath", back_populates="query", cascade="all, delete-orphan")


class AIResponse(Base):
    __tablename__ = "ai_responses"

    response_id = Column(Integer, primary_key=True, index=True)
    query_id = Column(Integer, ForeignKey("user_queries.query_id"), nullable=False)
    response_text = Column(Text, nullable=False)
    model_used = Column(String, nullable=False)  # gemini-1.5-pro or LaMini-Flan-T5-783M
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    query = relationship("UserQuery", back_populates="ai_response")


class Quiz(Base):
    __tablename__ = "quizzes"

    quiz_id = Column(Integer, primary_key=True, index=True)
    query_id = Column(Integer, ForeignKey("user_queries.query_id"), nullable=False)
    question_text = Column(Text, nullable=False)
    option_a = Column(String, nullable=False)
    option_b = Column(String, nullable=False)
    option_c = Column(String, nullable=False)
    option_d = Column(String, nullable=False)
    correct_answer = Column(String, nullable=False)  # A, B, C, or D
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    query = relationship("UserQuery", back_populates="quizzes")


class Summary(Base):
    __tablename__ = "summaries"

    summary_id = Column(Integer, primary_key=True, index=True)
    query_id = Column(Integer, ForeignKey("user_queries.query_id"), nullable=False)
    summary_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    query = relationship("UserQuery", back_populates="summaries")


class LearningPath(Base):
    __tablename__ = "learning_paths"

    path_id = Column(Integer, primary_key=True, index=True)
    query_id = Column(Integer, ForeignKey("user_queries.query_id"), nullable=False)
    topic = Column(String, nullable=False)
    difficulty_level = Column(String, nullable=False)  # e.g., Beginner, Intermediate, Advanced
    recommended_resources = Column(Text, nullable=False)  # Store list/details of resources as text or JSON block
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    query = relationship("UserQuery", back_populates="learning_paths")
