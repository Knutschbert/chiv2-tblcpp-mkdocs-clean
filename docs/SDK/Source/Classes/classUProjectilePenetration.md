---
title: UProjectilePenetration
type: class
aliases: UProjectilePenetration
share: false

---

# UProjectilePenetration





Inherits from [UAssemblyBlueprint](/docs/SDK/Source/Classes/classUAssemblyBlueprint.md), UBlueprint

## Public Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[[CanPenetrateActor]]**(AActor * HitActor) const |
| void | **[[InitPenetrationCollisionResponse]]**() |
| bool | **[[ShouldPenetrationAwardScore]]**(AActor * HitActor) const |
| | **[[UProjectilePenetration]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< TSubclassOf< AActor > > | **[[AllowedClasses]]**  |
| int32 | **[[AllowedNumPenetrations]]**  |
| FName | **[[DamageScoreEventName]]**  |
| float | **[[DamagerPerPenetrationMultiplier]]**  |
| FName | **[[KillScoreEventName]]**  |
| float | **[[PenetratableDamageMultiplier]]**  |
| bool | **[[bShouldAwardScoreOnPenetration]]**  |
| bool | **[[bShouldPenetratedChildrenOfAllowedClasses]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200