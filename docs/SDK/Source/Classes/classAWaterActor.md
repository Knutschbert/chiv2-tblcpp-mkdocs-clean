---
title: AWaterActor
type: class
aliases: AWaterActor
share: false

---

# AWaterActor





Inherits from [ATBLActor](/docs/SDK/Source/Classes/classATBLActor.md), [IProjectileOverlapEventInterface](/docs/SDK/Source/Classes/classIProjectileOverlapEventInterface.md), AActor, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[AWaterActor]]**() |
| void | **[[OnKilled]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) Event) |
| void | **[[OnWaterMeshBeginOverlap]]**(UPrimitiveComponent * OverlappedComponent, AActor * OtherActor, UPrimitiveComponent * OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult & SweepResult) |
| void | **[[OnWaterOverlapEvent]]**(AActor * Actor, FVector Location) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| UStaticMeshComponent * | **[[StaticMesh]]**  |
| float | **[[ZPlanExtent]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200