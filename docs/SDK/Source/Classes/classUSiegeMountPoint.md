---
title: USiegeMountPoint
type: class
aliases: USiegeMountPoint
share: false

---

# USiegeMountPoint





Inherits from USceneComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[BroadcastDismount]]**(EDismountType DismountType) |
| void | **[[BroadcastInterpToMountLocation]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| void | **[[BroadcastPendingSpawn]]**(bool bNewPendingSpawn) |
| bool | **[[CanMount]]**(APawn * Pawn) |
| void | **[[DismountPressed]]**() |
| void | **[[OnCharacterKilled]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & DamageEvent) |
| void | **[[OnCharacterKilledDuringInterp]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & DamageEvent) |
| void | **[[OnCombatStateChanged]]**(AActor * Actor, FName PreviousState, FName NewState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * CombatState) |
| void | **[[SetInteractableComponent]]**([UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * Interactable) |
| | **[[USiegeMountPoint]]**() |
| void | **[[UpdateInterpToMountLocation]]**(float DeltaSeconds) |
| void | **[[UsePressed]]**(APawn * InPawn, [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * InInteractable) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[CameraPitchRotationLimit]]**  |
| float | **[[CameraYawRotationLimit]]**  |
| TSubclassOf< [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) > | **[[CharacterAnimationSet]]**  |
| TSubclassOf< [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) > | **[[CharacterAnimationSet1P]]**  |
| FName | **[[CharacterAttachSocketName]]**  |
| int32 | **[[HorizLockId]]**  |
| float | **[[MaxMountAngle]]**  |
| float | **[[MaxMountAngleOffset]]**  |
| float | **[[MaxMountDistance]]**  |
| FName | **[[MountAnimation]]**  |
| [FMountBlendParams](/docs/SDK/Source/Classes/structFMountBlendParams.md) | **[[MountBlendParams]]**  |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[MountedCharacter]]**  |
| FRotator | **[[RotationLimitOffset]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[SiegeInventoryItem]]**  |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[SiegeInventoryItemClass]]**  |
| int32 | **[[VertLockId]]**  |
| uint8 | **[[bCanDismount]]**  |
| bool | **[[bUseMountCombatState]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200