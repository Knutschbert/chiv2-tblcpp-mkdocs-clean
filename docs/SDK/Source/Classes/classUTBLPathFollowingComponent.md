---
title: UTBLPathFollowingComponent
type: class
aliases: UTBLPathFollowingComponent
share: false

---

# UTBLPathFollowingComponent





Inherits from UCrowdFollowingComponent

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[UTBLPathFollowingComponent]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[OnBlockingActorExpired]]**() |
| void | **[[OnFinishedBlockedMovementResponse]]**() |
| void | **[[OnPathBlocked]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FVector | **[[NavLinkStart]]**  |
| FVector | **[[NavLinkTarget]]**  |
| bool | **[[bCannotCompletePath]]**  |
| bool | **[[bNavLinkWantsToJump]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[BlockStartTime]]**  |
| FTimerHandle | **[[BlockingActorExpiredTimer]]**  |
| FVector | **[[CurrentPathSegmentStart]]**  |
| FVector | **[[CurrentPathSegmentTarget]]**  |
| TWeakObjectPtr< AActor > | **[[LastKnownBlockingActor]]**  |
| FVector | **[[NavLinkMoveDestination]]**  |
| FAIRequestID | **[[NavLinkMoveRequestID]]**  |
| float | **[[PathBlockFailDuration]]**  |
| FTimerHandle | **[[PathBlockTimer]]**  |
| bool | **[[bDeferredPathUpdate]]**  |
| bool | **[[bPathInvalidatedDuringDefer]]**  |
| bool | **[[bPawnFellWhilePerformingBlockedMove]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200