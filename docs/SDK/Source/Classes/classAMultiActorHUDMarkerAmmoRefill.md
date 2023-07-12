---
title: AMultiActorHUDMarkerAmmoRefill
type: class
aliases: AMultiActorHUDMarkerAmmoRefill
share: false

---

# AMultiActorHUDMarkerAmmoRefill





Inherits from [AMultiActorHUDMarkerBase](/docs/SDK/Source/Classes/classAMultiActorHUDMarkerBase.md), AActor, [IHUDMarkerInterface](/docs/SDK/Source/Classes/classIHUDMarkerInterface.md), [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[AMultiActorHUDMarkerAmmoRefill]]**() |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * > | **[[CachedAmmoInventory]]**  |
| EFaction | **[[CachedFaction]]**  |
| [UInventory](/docs/SDK/Source/Classes/classUInventory.md) * | **[[CachedInventory]]**  |
| TArray< [FMarkedActorEntryAmmoRefill](/docs/SDK/Source/Classes/structFMarkedActorEntryAmmoRefill.md) > | **[[MarkedActors]]**  |
| float | **[[MaxMarkerDistance]]**  |
| float | **[[MaxMarkerDistanceSquared]]**  |
| int32 | **[[SimultaneousMarkerOverride]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200