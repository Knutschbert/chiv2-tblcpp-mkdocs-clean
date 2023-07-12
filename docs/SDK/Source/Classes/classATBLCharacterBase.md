---
title: ATBLCharacterBase
type: class
aliases: ATBLCharacterBase
share: false

---

# ATBLCharacterBase





Inherits from ACharacter, [ISignificanceInterface](/docs/SDK/Source/Classes/classISignificanceInterface.md)

Inherited by [ASiegeEngine](/docs/SDK/Source/Classes/classASiegeEngine.md), [ATBLAnimal](/docs/SDK/Source/Classes/classATBLAnimal.md), [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ATBLCharacterBase]]**() |
| void | **[[DisableMeshCollisionForFakeClient]]**() |
| void | **[[EnableMeshCollisionForFakeClient]]**() |
| float | **[[GetCreationTime]]**() |
| float | **[[GetDefaultFallDamageScale]]**() |
| float | **[[GetFallDamageScale]]**() |
| EMeshVisibilityFlag | **[[GetMeshVisibilityFlag]]**() const |
| float | **[[GetTimeSinceCharacterWasCarried]]**() const |
| bool | **[[IsAlive]]**() const |
| bool | **[[IsCustomizationCharacter]]**() |
| bool | **[[IsFirstPerson]]**() const |
| bool | **[[IsRagdollCustomTick]]**() const |
| bool | **[[IsTargetable]]**() const |
| void | **[[PostRecalcRequiredBones_Mesh1P]]**() |
| void | **[[PreRecalcRequiredBones_Mesh1P]]**() |
| void | **[[ServerTrapEvent]]**(ETrapEventResult Result, UObject * TrapObject, float ClientTimeStamp) |
| void | **[[SetCinematicSpawnInEnabled]]**(const UObject * WorldContextObject, bool bEnabled) |
| void | **[[SetFallDamageScale]]**(float InFallDamageScale) |
| void | **[[ShowThirdPersonMesh]]**() |
| void | **[[TrapEvent]]**(ETrapEventResult Result, UObject * TrapObject) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * | **[[FallDamageSource]]**  |
| float | **[[FallDamageStartingSpeed]]**  |
| TArray< [FPhysMatFallingDamageMultiplier](/docs/SDK/Source/Classes/structFPhysMatFallingDamageMultiplier.md) > | **[[FallingDamagePhysMatMultipliers]]**  |
| float | **[[HiddenAnimUpdateMaxDistance]]**  |
| int32 | **[[LastAnimUpdateRate]]**  |
| float | **[[LastCarryTime]]**  |
| EMeshVisibilityFlag | **[[MeshVisibilityFlag]]**  |
| [UTBLCharacterMovementBaseComponent](/docs/SDK/Source/Classes/classUTBLCharacterMovementBaseComponent.md) * | **[[MovementBase]]**  |
| FOnRecentlyRendered | **[[OnRecentlyRendered]]**  |
| FOnRootTransformUpdated | **[[OnRootTransformUpdated]]**  |
| [FCharacterSignificanceState](/docs/SDK/Source/Classes/structFCharacterSignificanceState.md) | **[[SignificanceState]]**  |
| bool | **[[SkipClientOptimizations]]**  |
| float | **[[ViewDistance]]**  |
| bool | **[[bIgnoreFaceRotation]]**  |
| bool | **[[bIsCarryableNPC]]**  |
| bool | **[[bIsIdleAnimation]]**  |
| bool | **[[bKillUponLanding]]**  |
| bool | **[[bMontageActive]]**  |
| bool | **[[bPlacedInWorld]]**  |
| bool | **[[bRootMotionActive]]**  |
| bool | **[[bWaitingForAnimNotify]]**  |
| bool | **[[bWasRecentlyRendered]]**  |
| bool | **[[bWeaponTracersActive]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200