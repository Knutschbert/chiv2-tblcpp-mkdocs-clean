---
title: AStrongholdBellTowerHudMarkerManager
type: class
aliases: AStrongholdBellTowerHudMarkerManager
share: false

---

# AStrongholdBellTowerHudMarkerManager





Inherits from AInfo

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[AStrongholdBellTowerHudMarkerManager]]**() |
| void | **[[ActivateManager]]**() |
| void | **[[DeactivateManager]]**() |
| void | **[[OnPlayerEnteredCapturePoint]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| void | **[[OnPlayerLeftCapturePoint]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| EFaction | **[[AttackingFaction]]**  |
| TArray< AActor * > | **[[CatapultActors]]**  |
| TArray< AActor * > | **[[CatapultAmmoActors]]**  |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[CatapultAmmoClass]]**  |
| TArray< AActor * > | **[[DestroyableActors]]**  |
| [FActorDisplayInfo](/docs/SDK/Source/Classes/structFActorDisplayInfo.md) | **[[LoadedCatapultDisplayInfo]]**  |
| [AMultiActorHUDMarker](/docs/SDK/Source/Classes/classAMultiActorHUDMarker.md) * | **[[MultiActorHUDMarker]]**  |
| AActor * | **[[TeamCapturePointActor]]**  |
| [FActorDisplayInfo](/docs/SDK/Source/Classes/structFActorDisplayInfo.md) | **[[UnLoadedCatapultDisplayInfo]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200