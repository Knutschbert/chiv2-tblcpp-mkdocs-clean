---
title: UBurnableComponent
type: class
aliases: UBurnableComponent
share: false

---

# UBurnableComponent





Inherits from UActorComponent

## Public Functions

|                | Name           |
| -------------- | -------------- |
| float | **[[GetTimeUntilBurnedDown]]**() const |
| void | **[[HandleOwnerDamageTaken]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & Event) |
| | **[[UBurnableComponent]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[ActorBoundingBoxTweak]]**  |
| TWeakObjectPtr< [UConditionsComponent](/docs/SDK/Source/Classes/classUConditionsComponent.md) > | **[[ConditionsComponent]]**  |
| [UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * | **[[DamageSource]]**  |
| TSubclassOf< [UFlammableStaticMeshComponent](/docs/SDK/Source/Classes/classUFlammableStaticMeshComponent.md) > | **[[FlammableStaticMeshComponentClass]]**  |
| FOnDamageAppliedToFlammableComponent | **[[OnDamageAppliedToFlammableComponent]]**  |
| float | **[[PercentHealth]]**  |
| float | **[[SphereCollisionRadius]]**  |
| TWeakObjectPtr< [UStatsComponent](/docs/SDK/Source/Classes/classUStatsComponent.md) > | **[[Stats]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200