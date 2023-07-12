---
title: UDrainStamina
type: class
aliases: UDrainStamina
share: false

---

# UDrainStamina





Inherits from UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[UDrainStamina]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[OnCombatStateEvent]]**(AActor * InActor, FName EventName, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo) |
| void | **[[OnDestroyed]]**(AActor * DestroyedActor) |
| void | **[[OnKilled]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & DamageEvent) |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< FName > | **[[CombatStates]]**  |
| int32 | **[[DisabledId]]**  |
| float | **[[DrainRate]]**  |
| UCurveFloat * | **[[DrainRateModifier]]**  |
| float | **[[LastTickTime]]**  |
| float | **[[Time]]**  |
| bool | **[[bEnabled]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200