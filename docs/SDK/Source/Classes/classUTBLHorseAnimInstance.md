---
title: UTBLHorseAnimInstance
type: class
aliases: UTBLHorseAnimInstance
share: false

---

# UTBLHorseAnimInstance





Inherits from [UTBLAnimInstance](/docs/SDK/Source/Classes/classUTBLAnimInstance.md), UAnimInstance

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AnimNotify_DeathAnim_End]]**() |
| void | **[[EventDamageNoInterrupt]]**(const [FAnimDamageParams](/docs/SDK/Source/Classes/structFAnimDamageParams.md) & DamageEvent) |
| void | **[[EventOnCombatStateChanged]]**(AActor * Actor, FName PreviousState, FName NewState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * InCombatState) |
| void | **[[EventOnDismounted]]**(EDismountType DismountType) |
| void | **[[EventOnHorseBump]]**(AActor * OtherActor, FName Direction, float Angle, float BumpVelocity, bool bRearImpact) |
| void | **[[EventOnHorseToCharacterImpact]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * TargetCharacter, EHorseImpactLocation ImpactLocation, EHorseToCharacterImpactType ImpactType, FName ImpactCombatState, float ImpactSpeed) |
| void | **[[EventOnHorseToHorseImpact]]**([AHorse](/docs/SDK/Source/Classes/classAHorse.md) * TargetHorse, EHorseImpactLocation ImpactLocation, EHorseToHorseImpactType ImpactType, FName ImpactCombatState, float ImpactSpeed) |
| void | **[[EventOnHorseToWorldImpact]]**(FHitResult Hit, EHorseImpactLocation ImpactLocation, EHorseToWorldImpactType ImpactType, FName ImpactCombatState, float ImpactSpeed) |
| void | **[[EventOnInterrupt]]**(const [FAnimDamageParams](/docs/SDK/Source/Classes/structFAnimDamageParams.md) & DamageEvent) |
| void | **[[EventOnKilled]]**() |
| void | **[[EventOnKnockdown]]**(const [FAnimDamageParams](/docs/SDK/Source/Classes/structFAnimDamageParams.md) & DamageEvent) |
| void | **[[EventOnMounted]]**(FName Direction) |
| void | **[[EventOnMovementActionStarted]]**(FName MovementName, FRotator Direction) |
| void | **[[EventOnMovementDirectionChanged]]**() |
| void | **[[EventOnMovementStateChanged]]**(FName InMovementState, FName InPreviousMovementState) |
| void | **[[EventOnRiderCombatStateChanged]]**(AActor * Actor, FName PreviousState, FName NewState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * InCombatState) |
| void | **[[EventOnStagger]]**(const [FAnimDamageParams](/docs/SDK/Source/Classes/structFAnimDamageParams.md) & DamageEvent) |
| void | **[[EventOnStartAttack]]**(FName InAbilityName, FName InCombatState, FName InComboState, [UAttackType](/docs/SDK/Source/Classes/classUAttackType.md) * InAttackType) |
| void | **[[EventOnStartDismount]]**(FName Direction) |
| void | **[[EventOnWantsToGallop]]**(bool bWantsToGallop) |
| FVector | **[[GetHorseMomentumBasedScale]]**(AActor * InitiatorActor, FName AbilityName, TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > InventoryItemClass) |
| bool | **[[IsPlayingMountAnimation]]**() |
| void | **[[OnAnimationSetChanged]]**(TSubclassOf< [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) > AnimationSet) |
| void | **[[OnCombatStateChanged]]**(AActor * Actor, FName PreviousState, FName NewState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * InCombatState) |
| void | **[[OnCombatStateEvent]]**(AActor * Actor, FName EventName, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo) |
| void | **[[OnCrowdControl]]**(FName InCombatState, const [FAnimDamageParams](/docs/SDK/Source/Classes/structFAnimDamageParams.md) & DamageEvent, ECrowdControlVariant CrowdControlVariant) |
| void | **[[OnCrowdControlNoDamage]]**(AActor * OwningActor, FName InCombatState, [FCrowdControlParams](/docs/SDK/Source/Classes/structFCrowdControlParams.md) CrowdControlParams) |
| void | **[[OnDismounted]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Driver, EDismountType DismountType) |
| void | **[[OnInterpToMountLocation]]**(FName AnimationName, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| void | **[[OnKickNoDriver]]**() |
| void | **[[OnKilled]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & DamageEvent) |
| void | **[[OnMounted]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Driver) |
| void | **[[OnMovementActionFinished]]**(FName MovementName) |
| void | **[[OnMovementActionStarted]]**(FName MovementName, FRotator Direction) |
| void | **[[OnPostDamage]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & DamageEvent, const [FPostDamageEventInfo](/docs/SDK/Source/Classes/structFPostDamageEventInfo.md) & PostDamageInfo) |
| void | **[[OnRiderCombatStateChanged]]**(AActor * Actor, FName PreviousState, FName NewState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * InCombatState) |
| void | **[[OnRiderCombatStateEvent]]**(AActor * Actor, FName EventName, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo) |
| void | **[[OnSignificanceChanged]]**(ECharacterSignificanceLevel InSignificance) |
| void | **[[OnStartAttack]]**() |
| void | **[[PlayDismountAnimation]]**(FName AnimationName) |
| void | **[[PlayLandedAnimation]]**() |
| void | **[[PlayMountAnimation]]**(FName AnimationName) |
| void | **[[StopDismountAnimation]]**() |
| | **[[UTBLHorseAnimInstance]]**() |
| void | **[[UpdateFootStepSounds]]**(float DeltaSeconds, bool bHidden) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[AimDirection]]**  |
| [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * | **[[AnimationSetBase]]**  |
| TArray< FName > | **[[AttackCombatStates]]**  |
| float | **[[CameraRelativeFacingAngle]]**  |
| float | **[[CameraRelativeInputAngle]]**  |
| FName | **[[CombatState]]**  |
| UAnimMontage * | **[[CurrentAttackMontage]]**  |
| float | **[[CurrentGroundSpeed]]**  |
| float | **[[CurrentSpeed]]**  |
| TMap< FName, FName > | **[[DeathMontages]]**  |
| UAnimMontage * | **[[DismountMontage]]**  |
| bool | **[[HasRider]]**  |
| [AHorse](/docs/SDK/Source/Classes/classAHorse.md) * | **[[Horse]]**  |
| [UHorseMovement](/docs/SDK/Source/Classes/classUHorseMovement.md) * | **[[HorseMovement]]**  |
| bool | **[[IsDead]]**  |
| bool | **[[IsLunge]]**  |
| TMap< FName, FName > | **[[MountUpSections]]**  |
| float | **[[MovementAcceleration]]**  |
| float | **[[MovementDirection]]**  |
| FName | **[[MovementState]]**  |
| float | **[[MovementStateMaxSpeed]]**  |
| float | **[[MovementStateWeight]]**  |
| FAnimNotifyStepEvent | **[[OnAnimNotifyStepEvent]]**  |
| TSubclassOf< [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) > | **[[PreviewAnimationSet]]**  |
| float | **[[PreviousInputDirection]]**  |
| FName | **[[PreviousMovementState]]**  |
| float | **[[PreviousSpeed]]**  |
| float | **[[PreviousTurnRate]]**  |
| FVector2D | **[[ProcessedInput]]**  |
| [UTBLCharacterAnimInstance_Playable](/docs/SDK/Source/Classes/classUTBLCharacterAnimInstance__Playable.md) * | **[[RiderAnimBP]]**  |
| TMap< FName, FName > | **[[RiderCrowdControlMontage]]**  |
| TMap< FName, FName > | **[[RiderCrowdControlMontage1P]]**  |
| ECharacterSignificanceLevel | **[[SignificanceLevel]]**  |
| FRotator | **[[SlopeAngle]]**  |
| float | **[[SlopeWeight]]**  |
| float | **[[StrafeWeight]]**  |
| float | **[[TurnRate]]**  |
| float | **[[TurnRateAccel]]**  |
| float | **[[TurnRateAccelInterpSpeed]]**  |
| float | **[[TurnRateInterpSpeed]]**  |
| float | **[[TurnRateStopDelay]]**  |
| float | **[[TurnRateStopTime]]**  |
| bool | **[[WasRecentlyRendered]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200