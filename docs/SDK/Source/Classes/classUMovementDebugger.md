---
title: UMovementDebugger
type: class
aliases: UMovementDebugger
share: false

---

# UMovementDebugger





Inherits from UActorComponent

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[Animate]]**(float Scale) |
| void | **[[AutoSaveToFile]]**(bool bSendToServer, const FString & Directory) |
| void | **[[BackwardPressed]]**() |
| void | **[[ClientLoadFromFile]]**(const FString & Filename) |
| void | **[[ClientSendFrame]]**([FMovementDebugFrame](/docs/SDK/Source/Classes/structFMovementDebugFrame.md) DebugFrame, bool bSyncTimeStamp) |
| void | **[[CloseDebugger]]**() |
| void | **[[DecreaseFrameOffset]]**() |
| void | **[[DisplayDebugScrollDown]]**() |
| void | **[[DisplayDebugScrollReleased]]**() |
| void | **[[DisplayDebugScrollUp]]**() |
| void | **[[DrawDebug]]**(UCanvas * Canvas) |
| void | **[[DrawFrame]]**([FMovementDebugFrame](/docs/SDK/Source/Classes/structFMovementDebugFrame.md) & DebugFrame, FColor Clr) |
| void | **[[DrawPose]]**([FDebugDrawShapes](/docs/SDK/Source/Classes/structFDebugDrawShapes.md) & DebugDraw, FColor Clr) |
| void | **[[DrawStatLine]]**(FVector Start, FVector End, FColor Clr) |
| bool | **[[FindServerFrame]]**(TArray< [FMovementDebugFrame](/docs/SDK/Source/Classes/structFMovementDebugFrame.md) > & SearchFrames, [FMovementDebugFrame](/docs/SDK/Source/Classes/structFMovementDebugFrame.md) & ReturnFrame, float ClientTimeStamp, int32 Direction) |
| void | **[[FixClientTimeStamps]]**(TArray< [FMovementDebugFrame](/docs/SDK/Source/Classes/structFMovementDebugFrame.md) > & Frames) |
| void | **[[ForwardPressed]]**() |
| [FMovementDebugFrame](/docs/SDK/Source/Classes/structFMovementDebugFrame.md) | **[[GetClientFrame]]**() |
| int32 | **[[GetClientIndex]]**() |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| [FMovementDebugFrame](/docs/SDK/Source/Classes/structFMovementDebugFrame.md) | **[[GetServerFrame]]**() |
| void | **[[IncreaseFrameOffset]]**() |
| void | **[[LoadFromFile]]**(const FString & Filename) |
| void | **[[NextCharacter]]**() |
| void | **[[OnMovementSync]]**(float ClientTimeStamp, float DeltaTime) |
| void | **[[OnPossessed]]**(APawn * NewPawn) |
| void | **[[OnRep_Recording]]**() |
| void | **[[PlayReleased]]**() |
| void | **[[PreviousCharacter]]**() |
| void | **[[RecordBoneChain]]**([FDebugDrawShapes](/docs/SDK/Source/Classes/structFDebugDrawShapes.md) & DebugDraw, ACharacter * Pawn, FName BoneName, FColor Color) |
| void | **[[RecordCapsule]]**([FMovementDebugFrame](/docs/SDK/Source/Classes/structFMovementDebugFrame.md) & DebugFrame, ACharacter * Pawn, FColor Color) |
| void | **[[RecordOtherCharacter]]**([FMovementDebugSimualated](/docs/SDK/Source/Classes/structFMovementDebugSimualated.md) & OtherCharacter, [ATBLCharacterBase](/docs/SDK/Source/Classes/classATBLCharacterBase.md) * OtherChar, UNetConnection * Connection) |
| void | **[[RecordPose]]**([FDebugDrawShapes](/docs/SDK/Source/Classes/structFDebugDrawShapes.md) & DebugDraw, ACharacter * Pawn, FColor Color) |
| void | **[[SaveToFile]]**(const FString & Filename) |
| void | **[[ServerSaveToFile]]**(const FString & Filename) |
| void | **[[ServerSetClientIndex]]**(int32 Index) |
| void | **[[ServerSetClientTimeStamp]]**(float ClientTimeStamp, int32 Direction) |
| void | **[[ServerSetTargetCharacter]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * DebugTarget) |
| void | **[[SetTargetCharacter]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| void | **[[StartRecord]]**() |
| void | **[[StopRecord]]**() |
| void | **[[Teleport]]**() |
| void | **[[ToggleDrawClient]]**() |
| void | **[[ToggleDrawServer]]**() |
| void | **[[ToggleRecord]]**() |
| | **[[UMovementDebugger]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< FName > | **[[BoneNames]]**  |
| float | **[[DebugPositionIndex]]**  |
| int32 | **[[DisplayDebugScrollDir]]**  |
| float | **[[DisplayDebugScrollY]]**  |
| int32 | **[[FrameOffset]]**  |
| int32 | **[[ID]]**  |
| UInputComponent * | **[[InputComponent]]**  |
| FString | **[[LastSavedFileName]]**  |
| int32 | **[[OtherCharacterIndex]]**  |
| int32 | **[[PlayDirection]]**  |
| float | **[[PlayDirectionDelay]]**  |
| TArray< [FMovementDebugFrame](/docs/SDK/Source/Classes/structFMovementDebugFrame.md) > | **[[RecordedFrames]]**  |
| [FMovementDebugFrame](/docs/SDK/Source/Classes/structFMovementDebugFrame.md) | **[[ServerFrame]]**  |
| TArray< [FMovementDebugFrame](/docs/SDK/Source/Classes/structFMovementDebugFrame.md) > | **[[ServerFramesFromFile]]**  |
| int32 | **[[ServerSyncFrame]]**  |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[TargetCharacter]]**  |
| bool | **[[bDrawClient]]**  |
| bool | **[[bDrawServer]]**  |
| bool | **[[bRecording]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200