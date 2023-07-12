---
title: ATBLPlayerCameraManager
type: class
aliases: ATBLPlayerCameraManager
share: false

---

# ATBLPlayerCameraManager





Inherits from APlayerCameraManager

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ATBLPlayerCameraManager]]**() |
| void | **[[DisableDeathCam]]**(bool bImmediate) |
| void | **[[DisableSpawnFadeOut]]**() |
| void | **[[EnableDeathCam]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * KilledCharacter) |
| void | **[[EnableDeathCam_1P]]**(AActor * Killed) |
| void | **[[EnableSpawnFadeOut]]**(float Duration) |
| AActor * | **[[GetActualViewTarget]]**() const |
| bool | **[[IsSpawnFadeOutEnabled]]**() const |
| void | **[[OnPlayerMeshChanged]]**(USkeletalMeshComponent * OldMesh, USkeletalMeshComponent * NewMesh) |
| bool | **[[ShouldDoSpawnFadeOut]]**() const |
| void | **[[ToggleSpectatorCamera]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| UCameraComponent * | **[[GetActiveCameraComponent]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [UCameraModifier_BlendInRotation](/docs/SDK/Source/Classes/classUCameraModifier__BlendInRotation.md) * | **[[CameraBlendInRotation]]**  |
| [UCameraModifier_CancelRotation](/docs/SDK/Source/Classes/classUCameraModifier__CancelRotation.md) * | **[[CameraCancelRotationMod]]**  |
| [UCameraModifier_DeathCam](/docs/SDK/Source/Classes/classUCameraModifier__DeathCam.md) * | **[[CameraDeathMod]]**  |
| [UCameraModifier_DeathCam1P](/docs/SDK/Source/Classes/classUCameraModifier__DeathCam1P.md) * | **[[CameraDeathMod_1P]]**  |
| [UCameraModifier_Offset](/docs/SDK/Source/Classes/classUCameraModifier__Offset.md) * | **[[CameraOffsetMod]]**  |
| [UCameraModifier_TurnLimit](/docs/SDK/Source/Classes/classUCameraModifier__TurnLimit.md) * | **[[CameraTurnLimitMod]]**  |
| [UCameraModifier_Zoom](/docs/SDK/Source/Classes/classUCameraModifier__Zoom.md) * | **[[CameraZoomMod]]**  |
| UPostProcessComponent * | **[[CharacterStatesPostProcessComponent]]**  |
| [FLastSpectatorPOV](/docs/SDK/Source/Classes/structFLastSpectatorPOV.md) | **[[LastSpectatorPOV]]**  |
| UPostProcessComponent * | **[[OutOfCombatPostProcessComponent]]**  |
| bool | **[[bDisableCameraAnims]]**  |
| bool | **[[bIsFirstPerson]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [UCameraModifier_ArrowCam](/docs/SDK/Source/Classes/classUCameraModifier__ArrowCam.md) * | **[[ArrowCam]]**  |
| TSubclassOf< [UCameraModifier_DeathCam](/docs/SDK/Source/Classes/classUCameraModifier__DeathCam.md) > | **[[CameraDeathModClass]]**  |
| TSubclassOf< [UCameraModifier_DeathCam1P](/docs/SDK/Source/Classes/classUCameraModifier__DeathCam1P.md) > | **[[CameraDeathModClass_1P]]**  |
| TSubclassOf< [UCameraModifier_HorizontalLock](/docs/SDK/Source/Classes/classUCameraModifier__HorizontalLock.md) > | **[[CameraHorizontalLockModClass]]**  |
| int32 | **[[CameraModifierId]]**  |
| TMap< int32, [UCameraModifier_TurnLock](/docs/SDK/Source/Classes/classUCameraModifier__TurnLock.md) * > | **[[CameraModifiers]]**  |
| TMap< UClass *, [FPropertyModifiers](/docs/SDK/Source/Classes/structFPropertyModifiers.md) > | **[[CameraShakePropertyModifiers]]**  |
| TSubclassOf< [UCameraModifier_TurnLimit](/docs/SDK/Source/Classes/classUCameraModifier__TurnLimit.md) > | **[[CameraTurnLimitModClass]]**  |
| TSubclassOf< [UCameraModifier_VerticalLock](/docs/SDK/Source/Classes/classUCameraModifier__VerticalLock.md) > | **[[CameraVerticalLockModClass]]**  |
| [UCameraModifier_FollowAnimation](/docs/SDK/Source/Classes/classUCameraModifier__FollowAnimation.md) * | **[[FollowAnimation]]**  |
| [UCameraModifier_SpawnFadeOut](/docs/SDK/Source/Classes/classUCameraModifier__SpawnFadeOut.md) * | **[[SpawnFadeOut]]**  |
| bool | **[[bLoopCameraShake]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200