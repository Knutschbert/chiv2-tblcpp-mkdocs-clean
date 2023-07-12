---
title: UProjectileCollision
type: class
aliases: UProjectileCollision
share: false

---

# UProjectileCollision





Inherits from UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[HandleDelayedHits]]**() |
| bool | **[[IgnoreCharactersBehind]]**(FHitResult Hit) const |
| void | **[[OnBeginOverlap]]**(UPrimitiveComponent * OverlappedComponent, AActor * Other, UPrimitiveComponent * OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult & OverlapInfo) |
| void | **[[OnHit]]**(UPrimitiveComponent * HitComponent, AActor * OtherActor, UPrimitiveComponent * OtherComp, FVector NormalImpulse, const FHitResult & Hit) |
| | **[[UProjectileCollision]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [UTBLProjectileMovementComponent](/docs/SDK/Source/Classes/classUTBLProjectileMovementComponent.md) * | **[[ProjectileMovement]]**  |
| TWeakObjectPtr< UShapeComponent > | **[[ShapeComponent]]**  |
| bool | **[[bCosmeticCollision]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200