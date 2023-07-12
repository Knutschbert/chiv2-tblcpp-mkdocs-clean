---
title: UWeaponRackComponent
type: class
aliases: UWeaponRackComponent
share: false

---

# UWeaponRackComponent





Inherits from [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md), UActorComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md), [IDisplayComponentInterface](/docs/SDK/Source/Classes/classIDisplayComponentInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[RefillItemsForPawn]]**(APawn * Pawn) |
| | **[[UWeaponRackComponent]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| bool | **[[GrantItemWithFullAmmo]]**  |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[ItemToGrant]]**  |
| UAkAudioEvent * | **[[ItemsAvailableLoopStart]]**  |
| UAkAudioEvent * | **[[ItemsAvailableLoopStop]]**  |
| UAkAudioEvent * | **[[ItemsNoLongerAvailable]]**  |
| UAkAudioEvent * | **[[ItemsNowAvailable]]**  |
| TArray< TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > > | **[[ItemsToRefill]]**  |
| FWeaponRackUsedSignature | **[[OnWeaponRackUsed]]**  |
| UAkComponent * | **[[OwningActorAudioComponent]]**  |
| bool | **[[RefillAllAmmoItems]]**  |
| int32 | **[[StacksToAdd]]**  |
| bool | **[[UseStackCountFromItem]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:01 +0200