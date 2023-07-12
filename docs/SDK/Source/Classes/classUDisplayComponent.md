---
title: UDisplayComponent
type: class
aliases: UDisplayComponent
share: false

---

# UDisplayComponent





Inherits from UActorComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md), [IDisplayComponentInterface](/docs/SDK/Source/Classes/classIDisplayComponentInterface.md)

Inherited by [UActorInfoDisplayComponent](/docs/SDK/Source/Classes/classUActorInfoDisplayComponent.md), [UHudMarkerDisplayComponent](/docs/SDK/Source/Classes/classUHudMarkerDisplayComponent.md), [UObjectiveStatusDisplayComponent](/docs/SDK/Source/Classes/classUObjectiveStatusDisplayComponent.md), [USimpleDisplayComponent](/docs/SDK/Source/Classes/classUSimpleDisplayComponent.md), [UUnderCrosshairDisplayComponent](/docs/SDK/Source/Classes/classUUnderCrosshairDisplayComponent.md), [UZoneDisplayComponent](/docs/SDK/Source/Classes/classUZoneDisplayComponent.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| EFaction | **[[GetFactionFromRelevantFaction]]**(EFactionOrAttackerDefender RelevantFaction) |
| EFaction | **[[GetFactionFromRelevantFactionStatic]]**(UObject * WorldContextObject, EFactionOrAttackerDefender RelevantFaction) |
| | **[[UDisplayComponent]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TSoftClassPtr< [UHUDContainerSubWidget](/docs/SDK/Source/Classes/classUHUDContainerSubWidget.md) > | **[[WidgetClass]]**  |
| EWidgetContainer | **[[WidgetContainerType]]**  |
| bool | **[[bCanHudMarkerUsePooledWidget]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200