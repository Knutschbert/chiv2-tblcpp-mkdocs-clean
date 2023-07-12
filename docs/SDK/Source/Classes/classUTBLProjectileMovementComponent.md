---
title: UTBLProjectileMovementComponent
type: class
aliases: UTBLProjectileMovementComponent
share: false

---

# UTBLProjectileMovementComponent





Inherits from UProjectileMovementComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[CleanupAbilityActors]]**() |
| void | **[[DisableAndDestroy]]**(float LifeSpan) |
| void | **[[EventBlocked]]**(const FHitResult & Hit) |
| void | **[[EventHit]]**(const FHitResult & Hit) |
| bool | **[[IsFakeClientProjectile]]**() const |
| void | **[[OnBlocked]]**(AActor * OtherActor, UPrimitiveComponent * OtherComp, FVector NormalImpulse, const FHitResult & Hit) |
| void | **[[OnBounce]]**(const FHitResult & Hit) |
| void | **[[OnHit]]**(UPrimitiveComponent * HitComponent, AActor * OtherActor, UPrimitiveComponent * OtherComp, FVector NormalImpulse, const FHitResult & Hit) |
| void | **[[OnTornOff]]**() |
| void | **[[RemoveIgnoredCollisionActor]]**(AActor * ActorToRemove) |
| void | **[[StopOnBlockingHit]]**(const FHitResult & Hit) |
| | **[[UTBLProjectileMovementComponent]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[CleanupAbilityActorsInternal]]**(AController * Controller) |
| void | **[[OnKilled]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & DamageEvent) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[AccumulatedTickTime]]**  |
| FRotator | **[[AngularVelocity]]**  |
| FVector | **[[BounceVelocity]]**  |
| TWeakObjectPtr< [UProjectileCollision](/docs/SDK/Source/Classes/classUProjectileCollision.md) > | **[[CollisionHandler]]**  |
| TArray< TWeakObjectPtr< AActor > > | **[[CollisionIgnoreActors]]**  |
| float | **[[DistanceTravelled]]**  |
| TArray< FName > | **[[DoNotCollideWithTaggedActors]]**  |
| float | **[[Drag]]**  |
| float | **[[DrawStrengthModifier]]**  |
| float | **[[FacingEnemyMaxAngle]]**  |
| float | **[[FacingOtherMaxAngle]]**  |
| float | **[[FacingTargetTime]]**  |
| float | **[[FacingTeammateMaxAngle]]**  |
| [UTBLProjectileMovementComponent](/docs/SDK/Source/Classes/classUTBLProjectileMovementComponent.md) * | **[[FakeClientProjectile]]**  |
| float | **[[FakeClientSubStepDistanceTravelled]]**  |
| FVector | **[[FakeClientSubStepLocation]]**  |
| FVector | **[[FakeClientSubStepVelocity]]**  |
| [UTBLProjectileMovementComponent](/docs/SDK/Source/Classes/classUTBLProjectileMovementComponent.md) * | **[[FakeClientTarget]]**  |
| FFakeProjectileUpdate | **[[FakeProjectileUpdate]]**  |
| TArray< [FHitActorInfo](/docs/SDK/Source/Classes/structFHitActorInfo.md) > | **[[HitActors]]**  |
| FVector | **[[HitVelocity]]**  |
| float | **[[InitialNonCollisionTime]]**  |
| FRotator | **[[InitialRotation]]**  |
| FVector | **[[InitiatorLocationOnSpawn]]**  |
| FRotator | **[[InitiatorRotationOnSpawn]]**  |
| FHitResult | **[[LastHitResult]]**  |
| FBlockingHitSignature | **[[OnBlockingHit]]**  |
| FDisabledSignature | **[[OnDisabled]]**  |
| FBlockingHitSignature | **[[OnFakeClientBlockingHit]]**  |
| FMovementFinishedSignature | **[[OnMovementFinished]]**  |
| FMovementStartedSignature | **[[OnMovementStarted]]**  |
| TArray< [FHitActorInfo](/docs/SDK/Source/Classes/structFHitActorInfo.md) > | **[[OverlappedParryActors]]**  |
| float | **[[ProjectileStartTime]]**  |
| float | **[[TornOffLifeSpan]]**  |
| bool | **[[bDoNotCollideWithEnemies]]**  |
| bool | **[[bDoNotCollideWithProjectiles]]**  |
| bool | **[[bDoNotCollideWithTeammates]]**  |
| bool | **[[bEnableDragging]]**  |
| bool | **[[bFakeClient]]**  |
| bool | **[[bFakeClientDestroyed]]**  |
| bool | **[[bFakeClientOffset]]**  |
| bool | **[[bFakeClientSubStep]]**  |
| bool | **[[bFixedSubstepOnServer]]**  |
| bool | **[[bParryImmediately]]**  |
| bool | **[[bParryImmediatelyTeammates]]**  |
| bool | **[[bUseProjectileControlComponent]]**  |
| bool | **[[bWaitForAbilities]]**  |
| bool | **[[bWasLastHitBlocked]]**  |
| bool | **[[bWasTickedThisFrame]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| bool | **[[bDelayedKill]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200