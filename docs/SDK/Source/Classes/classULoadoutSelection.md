---
title: ULoadoutSelection
type: class
aliases: ULoadoutSelection
share: false

---

# ULoadoutSelection





Inherits from UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| TArray< EWeaponTag > | **[[GetAllItemWeaponTagsFromLoadout]]**() |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[GetItemForSlot]]**(EInventoryItemSlot Slot, int32 Index) |
| TArray< TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > > | **[[GetItemSelectionBySlot]]**(EInventoryItemSlot Slot, bool bOnPickup) |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[GetRandomItemForSlot]]**(EInventoryItemSlot Slot) |
| | **[[ULoadoutSelection]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< TSubclassOf< [UWeaponGroup](/docs/SDK/Source/Classes/classUWeaponGroup.md) > > | **[[Bandage]]**  |
| TArray< EInventoryItemSlot > | **[[DisabledSlots]]**  |
| TArray< TSubclassOf< [UWeaponGroup](/docs/SDK/Source/Classes/classUWeaponGroup.md) > > | **[[Item]]**  |
| TArray< TSubclassOf< [UWeaponGroup](/docs/SDK/Source/Classes/classUWeaponGroup.md) > > | **[[Knife]]**  |
| TMap< TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) >, int32 > | **[[OverrideStackCount]]**  |
| TArray< TSubclassOf< [UWeaponGroup](/docs/SDK/Source/Classes/classUWeaponGroup.md) > > | **[[Primary]]**  |
| TArray< TSubclassOf< [UWeaponGroup](/docs/SDK/Source/Classes/classUWeaponGroup.md) > > | **[[Secondary]]**  |
| TArray< TSubclassOf< [UWeaponGroup](/docs/SDK/Source/Classes/classUWeaponGroup.md) > > | **[[Shield]]**  |
| TArray< TSubclassOf< [UWeaponGroup](/docs/SDK/Source/Classes/classUWeaponGroup.md) > > | **[[Special]]**  |
| TArray< EInventoryItemSlot > | **[[StartingSlots]]**  |
| bool | **[[bSpawnFists]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > > | **[[CachedItems]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200