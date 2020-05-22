from typing import List

from pydantic import BaseModel, Field


class Position(BaseModel):
    x: int = Field(default=0)
    y: int = Field(default=0)


class CollisionBox(Position):
    height: int = Field(default=0)
    width: int = Field(default=0)


class TypeConfig(BaseModel):
    collisionBoxes: List[CollisionBox] = Field(default=None)
    height: int = Field(default=0)
    minGap: int = Field(default=0)
    minSpeed: int = Field(default=0)
    multipleSpeed: int = Field(default=0)
    type: str = Field(default='')
    width: int = Field(default=0)
    yPos: int = Field(default=0)


class TrexConfig(BaseModel):
    DROP_VELOCITY: int
    GRAVITY: float
    HEIGHT: int
    INIITAL_JUMP_VELOCITY: int
    MAX_JUMP_HEIGHT: int
    MIN_JUMP_HEIGHT: int
    SPEED_DROP_COEFFICIENT: int
    SPRITE_WIDTH: int
    START_X_POS: int
    WIDTH: int


class Trex(BaseModel):
    jumpCount: int
    jumpVelocity: float
    minJumpHeight: int
    reachedMinHeight: bool
    speedDrop: bool
    spritePos: Position
    status: str
    xPos: int
    yPos: int


class Obstacle(BaseModel):
    collisionBoxes: List[CollisionBox] = Field(default=None)
    gap: int = Field(default=0)
    gapCoefficient: float = Field(default=0)
    size: int = Field(default=0)
    speedOffset: int = Field(default=0)
    spritePos: Position = Field(default=None)
    typeConfig: TypeConfig = Field(default=None)
    width: int = Field(default=0)
    xPos: int = Field(default=0)
    yPos: int = Field(default=0)
