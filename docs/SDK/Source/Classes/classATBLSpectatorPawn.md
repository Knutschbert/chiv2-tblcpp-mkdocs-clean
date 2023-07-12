---
title: ATBLSpectatorPawn
type: class
aliases: ATBLSpectatorPawn
share: false

---

# ATBLSpectatorPawn





Inherits from ASpectatorPawn

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ATBLSpectatorPawn]]**() |
| void | **[[ClearSpectatorCams]]**() |
| void | **[[EnableSmoothCameraMode]]**(int32 CameraNum) |
| void | **[[FreeCam]]**() |
| void | **[[Ghost]]**() |
| void | **[[GhostOff]]**() |
| bool | **[[IsGhost]]**() const |
| void | **[[LockSpectatorTranslationAxis]]**(FName AxisName, bool Blocked) |
| void | **[[NextCharacter]]**() |
| void | **[[PreviousCharacter]]**() |
| void | **[[SpectatorCam]]**(int32 CameraNum) |
| void | **[[SpectatorFollow]]**(const FString & PlayerName) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AddTurnAcceleration]]**(float Val, int32 Axis) |
| void | **[[DisplayDebugScrollDown]]**() |
| void | **[[DisplayDebugScrollReleased]]**() |
| void | **[[DisplayDebugScrollUp]]**() |
| void | **[[ProcessTurnAndLookInput]]**(const TEnumAsByte< EAxis::Type > Axis, const float Value) |
| void | **[[ProcessTurnAndLookInputRate]]**(const TEnumAsByte< EAxis::Type > Axis, const float Rate) |
| void | **[[UpdateOnCinematicStateChanged]]**(FGameplayTag PreviousStateTag, [UCinematicState](/docs/SDK/Source/Classes/classUCinematicState.md) * PreviousState, FGameplayTag NewStateTag, [UCinematicState](/docs/SDK/Source/Classes/classUCinematicState.md) * NewState) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| UCameraComponent * | **[[Camera]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| FRotator | **[[CachedViewRotation]]**  |
| [FSpectatorCameraConfig](/docs/SDK/Source/Classes/structFSpectatorCameraConfig.md) | **[[DefaultCamera]]**  |
| int32 | **[[DisplayDebugScrollDir]]**  |
| float | **[[DisplayDebugScrollY]]**  |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[FollowCharacter]]**  |
| APlayerState * | **[[FollowPlayerState]]**  |
| float | **[[InitialMaxSpeed]]**  |
| float | **[[LastResetIdleTime]]**  |
| float | **[[ResetIdleRate]]**  |
| TArray< [FSpectatorCameraConfig](/docs/SDK/Source/Classes/structFSpectatorCameraConfig.md) > | **[[SmoothCameras]]**  |
| TArray< [FSmoothSpectatorTurn](/docs/SDK/Source/Classes/structFSmoothSpectatorTurn.md) > | **[[SmoothTurn]]**  |
| TArray< [FSpectatorCamInfo](/docs/SDK/Source/Classes/structFSpectatorCamInfo.md) > | **[[SpectatorCameras]]**  |
| float | **[[TurnAcceleration]]**  |
| float | **[[TurnChangeDirBoost]]**  |
| float | **[[TurnDeceleration]]**  |
| float | **[[TurnMaxSpeed]]**  |
| int32 | **[[ZoomDir]]**  |
| float | **[[ZoomDistance]]**  |
| float | **[[ZoomMax]]**  |
| float | **[[ZoomMin]]**  |
| float | **[[ZoomStartTime]]**  |
| bool | **[[bDidAutoSpectatorFollow]]**  |
| bool | **[[bIsGhost]]**  |
| bool | **[[bResetIdleTime]]**  |
| bool | **[[bSpectatorRightStickSensitivityDecrease]]**  |
| bool | **[[bSpectatorRightStickSensitivityIncrease]]**  |
| bool | **[[bSpectatorRollHeld]]**  |
| bool | **[[bSpectatorSpeedDown]]**  |
| bool | **[[bSpectatorSpeedUp]]**  |
| bool | **[[bUseCachedViewRotation]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200