---
title: UInputReplayComponent
type: class
aliases: UInputReplayComponent
share: false

---

# UInputReplayComponent





Inherits from UActorComponent

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AutoInputRec]]**() |
| void | **[[InputAppend]]**(const FString & NewReplayName, const FString & ReplayName2) |
| void | **[[InputCopyToOtherChars]]**(const FString & NewReplayName) |
| void | **[[InputPlay]]**(const FString & NewReplayName) |
| void | **[[InputRec]]**(const FString & NewReplayName) |
| void | **[[InputStop]]**() |
| void | **[[SaveAutoInputRecord]]**() |
| | **[[UInputReplayComponent]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AdvanceFrame]]**() |
| void | **[[ClearInput]]**() |
| void | **[[DoFrame]]**(float DeltaTime) |
| void | **[[DoKeyEvent]]**(uint8 KeyBind, TEnumAsByte< EInputEvent > KeyEvent) |
| [FReplayCharacterState](/docs/SDK/Source/Classes/structFReplayCharacterState.md) | **[[GetCharacterState]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| int32 | **[[GetCurrentFrame]]**() |
| [UInputReplay](/docs/SDK/Source/Classes/classUInputReplay.md) * | **[[GetInputReplay]]**() |
| int32 | **[[GetNumFrames]]**() |
| float | **[[GetRelativeFacingAngle]]**(AActor * Actor) |
| FVector | **[[GetRelativeLocation]]**(AActor * Actor) |
| void | **[[SetReplayState]]**(TEnumAsByte< EInputReplayState::Type > NewReplayState) |
| void | **[[UpdateReplay]]**(float DeltaTime) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FRotator | **[[TargetRotation]]**  |
| bool | **[[bValidRotation]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| int32 | **[[CurrentFrame]]**  |
| [FInputReplayValues](/docs/SDK/Source/Classes/structFInputReplayValues.md) | **[[InputFrame]]**  |
| [UInputReplay](/docs/SDK/Source/Classes/classUInputReplay.md) * | **[[InputReplay]]**  |
| FRotator | **[[LastControlRotation]]**  |
| float | **[[PlaybackFrameTime]]**  |
| TArray< uint8 > | **[[PlaybackPressed]]**  |
| FString | **[[ReplayName]]**  |
| TEnumAsByte< EInputReplayState::Type > | **[[ReplayState]]**  |
| bool | **[[bAutoInputRec]]**  |
| bool | **[[bDoObjective]]**  |
| bool | **[[bNewReplayFrame]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200