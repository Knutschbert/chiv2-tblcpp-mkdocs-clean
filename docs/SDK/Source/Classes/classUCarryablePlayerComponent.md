---
title: UCarryablePlayerComponent
type: class
aliases: UCarryablePlayerComponent
share: false

---

# UCarryablePlayerComponent





Inherits from UActorComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| | **[[UCarryablePlayerComponent]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[[CanPickup]]**(APawn * Pawn) |
| void | **[[OnCarryableAnimationEvent]]**(FName EventName) |
| void | **[[OnCarryableItemDestroyed]]**(AActor * Actor) |
| void | **[[OnCharacterDestroyed]]**(AActor * Actor) |
| void | **[[OnCharacterKilled]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & Event) |
| void | **[[OnDropped]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character, FTransform Transform) |
| void | **[[OnFakeClientProjectileHit]]**(const [FProjectileHitParams](/docs/SDK/Source/Classes/structFProjectileHitParams.md) & HitParams) |
| void | **[[OnInteractableEnabled]]**(bool bEnabled) |
| void | **[[OnPreThrown]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character, FTransform Transform) |
| void | **[[OnRep_CarryableItem]]**() |
| void | **[[OnRootTransformUpdated]]**() |
| void | **[[OnSetAttached]]**(bool bAttached) |
| void | **[[OnSpawnFakeClient]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * FakeClient) |
| void | **[[OnThrown]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character, FTransform Transform) |
| void | **[[OnUse]]**(APawn * Pawn, [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * Interactable) |
| void | **[[OnUseHeld]]**(APawn * Pawn, float UseTime, [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * Interactable) |
| void | **[[OnUseReleased]]**(APawn * Pawn, float UseTime) |
| void | **[[StartPickup]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[CarryableItemClass]]**  |
| FRotator | **[[RelativeCarryRotation]]**  |
| float | **[[RelativeLandingYawOffset]]**  |
| FRotator | **[[RelativeThrownRotation]]**  |
| float | **[[YawRotationLimit]]**  |
| bool | **[[bCanKillOnThrow]]**  |
| bool | **[[bCanPickupFromDowned]]**  |
| bool | **[[bCanRevive]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| FTransform | **[[CachedOwnerItemDroppedTransform]]**  |
| [FReplicated_AInventoryItem](/docs/SDK/Source/Classes/structFReplicated__AInventoryItem.md) | **[[CarryableItem]]**  |
| int32 | **[[HorizLockId]]**  |
| [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * | **[[InteractableComponent]]**  |
| [ATBLCharacterBase](/docs/SDK/Source/Classes/classATBLCharacterBase.md) * | **[[OwnerCharacter]]**  |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[ParentCharacter]]**  |
| bool | **[[bCachedRVOEnabled]]**  |
| bool | **[[bHeldByEnemy]]**  |
| bool | **[[bIsBeingHeld]]**  |
| bool | **[[bOnRootTransformUpdate]]**  |
| bool | **[[bUsedFakedClientDrop]]**  |
| bool | **[[bUsedFakedClientThrow]]**  |
| bool | **[[bWasThrown]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200