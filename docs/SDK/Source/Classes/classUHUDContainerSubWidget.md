---
title: UHUDContainerSubWidget
type: class
aliases: UHUDContainerSubWidget
share: false

---

# UHUDContainerSubWidget





Inherits from UUserWidget

Inherited by [UHUDMarkerContainerSubWidget](/docs/SDK/Source/Classes/classUHUDMarkerContainerSubWidget.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| AActor * | **[[GetAssignedActor]]**() const |
| void | **[[K2_OnAssignedToActor]]**(AActor * Actor, UActorComponent * Component) |
| void | **[[K2_OnFocusedChanged]]**(bool bInIsFocused) |
| void | **[[K2_OnReturnedToPool]]**() |
| void | **[[K2_UpdateFocusParams]]**(float InAlpha, float InScale) |
| | **[[UHUDContainerSubWidget]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| AActor * | **[[AssignedActor]]**  |
| UActorComponent * | **[[AssignedComponent]]**  |
| float | **[[FocusAlpha]]**  |
| float | **[[FocusScale]]**  |
| bool | **[[bIsFocused]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200