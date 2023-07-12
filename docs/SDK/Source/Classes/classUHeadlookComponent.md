---
title: UHeadlookComponent
type: class
aliases: UHeadlookComponent
share: false

---

# UHeadlookComponent





Inherits from UActorComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[GetHeadlookLocation]]**(FVector & OutHeadlookLocation, bool & OutIsHeadlook) |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| void | **[[SetTargetActor]]**(AActor * Target) |
| | **[[UHeadlookComponent]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[DistanceSquaredToLocalNearestActor]]**  |
| AActor * | **[[LocalNearestActor]]**  |
| AActor * | **[[TargetActor]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200