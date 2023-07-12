---
title: UPushingComponent
type: class
aliases: UPushingComponent
share: false

---

# UPushingComponent





Inherits from UActorComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| void | **[[SetPushingDirection]]**(EPushingDirection Direction) |
| | **[[UPushingComponent]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[[FindOverlappingCharacters]]**(TArray< [ATBLCharacterBase](/docs/SDK/Source/Classes/classATBLCharacterBase.md) * > & OutCharacters, FVector Offset) |
| TArray< UPrimitiveComponent * > | **[[GetCollisionComponents]]**() |
| FVector | **[[GetFallingPushDirection]]**(AActor * PushingActor, AActor * OtherActor, float DeltaSeconds) |
| FVector | **[[GetOwnerVelocity]]**() |
| FVector | **[[GetPushVelocity]]**(AActor * PushingActor, AActor * OtherActor) |
| float | **[[GetPushingRadius]]**(AActor * Actor) |
| bool | **[[HasEqualPriority]]**(AActor * OtherActor) |
| void | **[[OnCharacterMovementUpdated]]**(float DeltaSeconds, FVector OldLocation, FVector OldVelocity) |
| void | **[[OnRep_DesiredPushedVelocity]]**() |
| void | **[[OnRep_PushingPriority]]**() |
| void | **[[PushActor]]**(AActor * Actor, FVector PushVel) |
| void | **[[SetPushedVelocity]]**(FVector PushVel) |
| bool | **[[ShouldPush]]**(AActor * OtherActor) |
| void | **[[UpdatePushed]]**(float DeltaTime) |
| void | **[[UpdatePushing]]**(float DeltaSeconds, const FVector & OldLocation) |
| void | **[[UpdatePushingWhileFalling]]**(float DeltaSeconds) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FName | **[[CollisionProfileName]]**  |
| float | **[[FallingOverlapOffset]]**  |
| float | **[[FallingPushBackSpeed]]**  |
| float | **[[FallingPushSpeed]]**  |
| float | **[[MaxPushSpeed]]**  |
| float | **[[MinPushSpeed]]**  |
| FPushingOverlapCharacters | **[[OnOverlapCharacters]]**  |
| FVector | **[[PushedVelocity]]**  |
| bool | **[[bCannotBePushed]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| int32 | **[[BasePushingPriority]]**  |
| [FReplicated_FVector](/docs/SDK/Source/Classes/structFReplicated__FVector.md) | **[[DesiredPushedVelocity]]**  |
| FVector | **[[PreviousLocation]]**  |
| [FPushOverTime](/docs/SDK/Source/Classes/structFPushOverTime.md) | **[[PushOverTimeParams]]**  |
| float | **[[PushedTime]]**  |
| EPushingDirection | **[[PushingDirection]]**  |
| int32 | **[[PushingInstanceId]]**  |
| TMap< int32, int32 > | **[[PushingInstances]]**  |
| [FReplicated_Int32](/docs/SDK/Source/Classes/structFReplicated__Int32.md) | **[[PushingPriority]]**  |
| FVector | **[[Velocity]]**  |
| bool | **[[bOwnerIsCharacter]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200