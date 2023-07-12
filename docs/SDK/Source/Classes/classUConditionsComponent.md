---
title: UConditionsComponent
type: class
aliases: UConditionsComponent
share: false

---

# UConditionsComponent





Inherits from UActorComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[ApplyCondition]]**(EConditionType Condition, AActor * DamageCauser, [UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * DamageSource) |
| bool | **[[GetDownedCanGetUp]]**() const |
| float | **[[GetDownedScore]]**() const |
| float | **[[GetDownedScorePercent]]**() const |
| float | **[[GetDownedTime]]**() const |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| float | **[[GetMaxDownedScore]]**() const |
| void | **[[HandleOwnerDamageTaken]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & Event) |
| void | **[[HandleOwnerPreBroadcastDamage]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & DamageTakenEvent) |
| bool | **[[HasCondition]]**(EConditionType Condition) const |
| void | **[[RemoveCondition]]**(EConditionType Condition, bool bClearStacks, AActor * ConditionRemover) |
| void | **[[Revive]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * RevivedBy) |
| void | **[[SetDownedScore]]**(float Score) |
| | **[[UConditionsComponent]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [UConditionsSpec](/docs/SDK/Source/Classes/classUConditionsSpec.md) * | **[[ConditionsSpec]]**  |
| FOnApplyCondition | **[[OnApplyCondition]]**  |
| FOnRemoveCondition | **[[OnRemoveCondition]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200