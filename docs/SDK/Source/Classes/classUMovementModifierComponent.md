---
title: UMovementModifierComponent
type: class
aliases: UMovementModifierComponent
share: false

---

# UMovementModifierComponent





Inherits from UActorComponent

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AddModifier]]**(FName Modifier) |
| bool | **[[HasModifier]]**(FName Modifier) |
| void | **[[RemoveModifier]]**(FName Modifier) |
| | **[[UMovementModifierComponent]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FName | **[[CurrentSlopeState]]**  |
| float | **[[DownhillMinAngle]]**  |
| UDataTable * | **[[MovementModifierDataTable]]**  |
| TMap< FName, [FMovementModifier](/docs/SDK/Source/Classes/structFMovementModifier.md) > | **[[MovementModifiers]]**  |
| TMap< UPhysicalMaterial *, FName > | **[[PhysMaterialModifiers]]**  |
| UPhysicalMaterial * | **[[PreviousPhysMaterial]]**  |
| float | **[[SlopeAngle]]**  |
| float | **[[TotalModifier]]**  |
| float | **[[UphillMinAngle]]**  |
| bool | **[[bDisableSprint]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200