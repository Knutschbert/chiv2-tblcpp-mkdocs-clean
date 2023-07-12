---
title: UTBLCharacterAnimInstance
type: class
aliases: UTBLCharacterAnimInstance
share: false

---

# UTBLCharacterAnimInstance





Inherits from [UTBLAnimInstance](/docs/SDK/Source/Classes/classUTBLAnimInstance.md), UAnimInstance

Inherited by [UTBLCharacterAnimInstance_Customization](/docs/SDK/Source/Classes/classUTBLCharacterAnimInstance__Customization.md), [UTBLCharacterAnimInstance_Peasant](/docs/SDK/Source/Classes/classUTBLCharacterAnimInstance__Peasant.md), [UTBLCharacterAnimInstance_Playable](/docs/SDK/Source/Classes/classUTBLCharacterAnimInstance__Playable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AnimNotify_DropWeapon]]**() |
| void | **[[AnimNotify_Revive]]**() |
| void | **[[AnimNotify_ShieldAttach]]**() |
| void | **[[AnimNotify_ShieldDetach]]**() |
| void | **[[AnimNotify_UseItem]]**() |
| void | **[[AnimNotify_WeaponAttach]]**() |
| void | **[[AnimNotify_WeaponDetach]]**() |
| void | **[[BlueprintOnAnimationSetChanged]]**() |
| void | **[[CarryableSectionChanged]]**(UAnimMontage * Montage, int32 NextSection) |
| void | **[[CustomizationStandToWeapon]]**(UAnimMontage * Montage, bool bInterrupted) |
| void | **[[CustomizationWeaponToStand]]**(UAnimMontage * Montage, bool bInterrupted) |
| void | **[[DisableAttackRootMotion]]**() |
| void | **[[DisableSpawnRootMotion]]**(FName AnimationName) |
| bool | **[[DoesAttackHaveActivateAbilityNotify]]**(FName AttackName) |
| void | **[[EventCarryableCharacter]]**(FName EventName, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * ParentCharacter) |
| void | **[[EventDamageNoInterrupt]]**(const [FAnimDamageParams](/docs/SDK/Source/Classes/structFAnimDamageParams.md) & DamageEvent) |
| void | **[[EventFreezeRagdollPhysics]]**() |
| void | **[[EventHiddenPositionUpdate]]**() |
| void | **[[EventOnCameraOffsetBegin]]**() |
| void | **[[EventOnCameraOffsetEnd]]**(float AngleOffset) |
| void | **[[EventOnCombatStateBegin]]**(AActor * Actor, FName State, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * InCombatState) |
| void | **[[EventOnCombatStateChanged]]**(AActor * Actor, FName PreviousState, FName NewState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * InCombatState) |
| void | **[[EventOnCombatStateEnd]]**(AActor * Actor, FName State, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * InCombatState) |
| void | **[[EventOnCrowdControl]]**(FName InCombatState, const [FAnimDamageParams](/docs/SDK/Source/Classes/structFAnimDamageParams.md) & DamageEvent, ECrowdControlVariant CrowdControlVariant) |
| void | **[[EventOnDash]]**(float InDashDirection) |
| void | **[[EventOnDashCooldownFinished]]**() |
| void | **[[EventOnDisarm]]**() |
| void | **[[EventOnGetUp]]**(FName Direction) |
| void | **[[EventOnHitAfterDeath]]**(const [FAnimDeathParams](/docs/SDK/Source/Classes/structFAnimDeathParams.md) & Params) |
| void | **[[EventOnHorseDismounted]]**(EDismountType DismountType) |
| void | **[[EventOnHorseMounted]]**() |
| void | **[[EventOnHorseStartDismount]]**(FName Direction) |
| void | **[[EventOnHorseStartMount]]**(FName Direction) |
| void | **[[EventOnInterrupt]]**(const [FAnimDamageParams](/docs/SDK/Source/Classes/structFAnimDamageParams.md) & DamageEvent) |
| void | **[[EventOnJump]]**() |
| void | **[[EventOnKilled]]**(const [FAnimDeathParams](/docs/SDK/Source/Classes/structFAnimDeathParams.md) & Params) |
| void | **[[EventOnLanded]]**() |
| void | **[[EventOnMeleeHitSuccess]]**(FName AttackName, FName AttackComboState) |
| void | **[[EventOnMissingLimb]]**(FName Condition) |
| void | **[[EventOnMovementActionStarted]]**(FName MovementName, FRotator Direction) |
| void | **[[EventOnMovementDirectionChanged]]**() |
| void | **[[EventOnMovementStateChanged]]**(FName InMovementState, FName InPreviousMovementState) |
| void | **[[EventOnSiegeDismounted]]**(EDismountType DismountType) |
| void | **[[EventOnSiegeMounted]]**() |
| void | **[[EventOnSignificanceChanged]]**() |
| void | **[[EventOnSprintStart]]**() |
| void | **[[EventOnSprintState]]**(FName SprintState) |
| void | **[[EventOnSprintStop]]**(bool bIsHoldingMoveKey) |
| void | **[[EventOnStartAttack]]**(FName InAbilityName, FName InCombatState, FName InComboState, [UAttackType](/docs/SDK/Source/Classes/classUAttackType.md) * InAttackType) |
| void | **[[EventOnStrafeStop]]**() |
| void | **[[EventOnWantsToGallop]]**(bool bWantsToGallop) |
| void | **[[EventSpawnMontageComplete]]**(const FName & AnimationName) |
| void | **[[EventSpawnMontageStart]]**(const FName & AnimationName) |
| void | **[[EventUnfreezeRagdollPhysics]]**() |
| void | **[[EventVOPlaying]]**(bool IsPlaying) |
| [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * | **[[GetAnimationSetFromData]]**([FAnimationSetDataTable](/docs/SDK/Source/Classes/structFAnimationSetDataTable.md) AnimInfo) |
| void | **[[GetCurrentLadderRootMotion]]**(FVector & OutTranslation, FRotator & OutRotation, FName SectionName, bool bEndAnimation) |
| void | **[[GetCurrentRootMotion]]**(FVector & OutTranslation, FRotator & OutRotation, UAnimMontage * Montage, FName SectionName, bool bEndAnimation, float Position) |
| float | **[[GetCurrentSpawnAnimationTime]]**() |
| void | **[[GetCurrentSpawnRootMotion]]**(FVector & OutTranslation, FRotator & OutRotation, FName AnimationName, float Position) |
| FVector | **[[GetHorseDismountOffset]]**(FName AnimationName) |
| float | **[[GetInventoryAnimationLength]]**() |
| FVector | **[[GetLadderMountOffset]]**(bool MountUp, bool bFromTop) |
| float | **[[GetMountAnimationLength]]**(bool MountUp, FName Direction) |
| float | **[[GetPeasantAnimationLength]]**(FName InCombatState) |
| float | **[[GetPhysicsSpawnTime]]**(FName AnimationName) |
| void | **[[GetSpawnMontage]]**(FName AnimationName, UAnimMontage *& Montage, FName & MontageName, FName & SectionName) |
| int32 | **[[GetStopAnimGraphValue]]**() |
| void | **[[HideBones]]**(TArray< FName > BoneList, TArray< FName > VisibleBones) |
| void | **[[HideUnusedBonesOnServer]]**() |
| void | **[[LadderMontageEnded]]**(UAnimMontage * Montage, bool bInterrupted) |
| void | **[[LadderSectionChanged]]**(UAnimMontage * Montage, int32 NextSection) |
| void | **[[NotifyCompleteDeathAnimation]]**() |
| void | **[[OnAnimationComplete]]**() |
| void | **[[OnAnimationSetChanged]]**(FName AnimSetName, [FAnimationSetDataTable](/docs/SDK/Source/Classes/structFAnimationSetDataTable.md) AnimInfo, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * InventoryItem) |
| void | **[[OnBackToIdleTimer]]**() |
| void | **[[OnCarryableCharacterEvent]]**(FName EventName, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * ParentCharacter) |
| void | **[[OnCarryableParent_CombatStateBegin]]**(AActor * Actor, FName InCombatStateName, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * InCombatState) |
| void | **[[OnChildAttachedToMesh]]**(USceneComponent * Child) |
| void | **[[OnCombatStateBegin]]**(AActor * Actor, FName State, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * InCombatState) |
| void | **[[OnCombatStateChanged]]**(AActor * Actor, FName PreviousState, FName NewState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * InCombatState) |
| void | **[[OnCombatStateEvent]]**(AActor * Actor, FName EventName, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo) |
| void | **[[OnConditionAdded]]**(AActor * Actor, EConditionType Condition) |
| void | **[[OnCrowdControl]]**(FName InCombatState, const [FAnimDamageParams](/docs/SDK/Source/Classes/structFAnimDamageParams.md) & DamageEvent, ECrowdControlVariant CrowdControlVariant) |
| void | **[[OnCrowdControlNoDamage]]**(AActor * OwningActor, FName InCombatState, [FCrowdControlParams](/docs/SDK/Source/Classes/structFCrowdControlParams.md) CrowdControlParams) |
| void | **[[OnCustomizationApplied]]**(const [FCustomizationContext](/docs/SDK/Source/Classes/structFCustomizationContext.md) & Context) |
| void | **[[OnDismount]]**(AActor * AttachParent, EDismountType DismountType) |
| void | **[[OnEquippedItemsChanged]]**() |
| void | **[[OnFreezeRagdollPhysics]]**() |
| void | **[[OnGetUp]]**(FName Direction) |
| void | **[[OnKilled]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & Event) |
| void | **[[OnMeleeSuccess]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * DamagedCharacter) |
| void | **[[OnMount]]**(AActor * AttachParent, [USiegeMountPoint](/docs/SDK/Source/Classes/classUSiegeMountPoint.md) * MountPoint) |
| void | **[[OnMovementActionFinished]]**(FName MovementName) |
| void | **[[OnMovementActionStarted]]**(FName MovementName, FRotator Direction) |
| void | **[[OnMovementStateChanged]]**(FName NewMovementState) |
| void | **[[OnMovementStateUpdate]]**(float DeltaSeconds) |
| void | **[[OnParryInEnded]]**(UAnimMontage * Montage, bool bInterrupted) |
| void | **[[OnParrySuccess]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * ThisCharacter, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * OtherCharacter, [FParryEventState](/docs/SDK/Source/Classes/structFParryEventState.md) ParryEventState) |
| void | **[[OnPostDamage]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & DamageEvent, const [FPostDamageEventInfo](/docs/SDK/Source/Classes/structFPostDamageEventInfo.md) & PostDamageInfo) |
| void | **[[OnRagdollHitFxEvent]]**(AActor * HitTaker, AActor * HitCauser, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Weapon, const FHitResult & HitResult, const FVector & HitDirection, float Damage, [UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * DamageSource, AActor * Projectile, FName AttackName) |
| void | **[[OnRecentlyRendered]]**(bool bInRecentlyRendered) |
| void | **[[OnResetForAnimInstancePool]]**() |
| void | **[[OnSetRagdollPhysics]]**() |
| void | **[[OnSignificanceChanged]]**(ECharacterSignificanceLevel InSignificance) |
| void | **[[OnSpawnAnimationComplete]]**(UAnimMontage * Montage, bool bInterrupted) |
| void | **[[OnSprintTurn]]**() |
| void | **[[OnStartAttack]]**() |
| void | **[[OnSwitchAttack]]**() |
| void | **[[OnUnfreezeRagdollPhysics]]**() |
| void | **[[OnVault]]**([AVaultMarker](/docs/SDK/Source/Classes/classAVaultMarker.md) * VaultMarker) |
| void | **[[OnWasHitEarly]]**(const [FEarlyHitResult](/docs/SDK/Source/Classes/structFEarlyHitResult.md) & EarlyHit) |
| void | **[[PlayCombatStateMontage]]**(FName InCombatState, FName MontageName, FName SectionName, [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * AnimSet) |
| void | **[[PlayDeathAnimation]]**() |
| void | **[[PlayHorseDismountAnimation]]**(FName AnimationName) |
| void | **[[PlayHorseLandedAnimation]]**() |
| void | **[[PlayHorseMountAnimation]]**(FName AnimationName) |
| void | **[[PlayInventoryAnimation]]**(FName Animation, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item) |
| float | **[[PlayInventoryItemEquipped]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item) |
| float | **[[PlayInventoryItemUnequipped]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item) |
| float | **[[PlayInventoryItemUse]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item, bool bPickup) |
| void | **[[PlayLadderAnimation]]**(FName SectionName) |
| void | **[[PlaySpawnAnimation]]**(FName AnimationName) |
| void | **[[ReverseLadderAnimation]]**() |
| void | **[[SetDeathAnimationParameters]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & Event, uint32 RandomSeed) |
| void | **[[SetOnHorse]]**(bool bIsOnHorse) |
| bool | **[[ShouldStopAnimGraph]]**() |
| void | **[[StartAttack]]**(bool bIsHeavy) |
| void | **[[StartParryAttack]]**([UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * AnimSet) |
| void | **[[StartPeasantAnimation]]**(FName InCombatState) |
| void | **[[StopCurrentCombatStateMontage]]**(FName NewCombatState, float BlendTime) |
| void | **[[TriggerRagdoll]]**() |
| | **[[UTBLCharacterAnimInstance]]**() |
| void | **[[UpdateFootStepSounds]]**(float DeltaSeconds, bool bHidden) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FName | **[[AbilityName]]**  |
| float | **[[AimPitch]]**  |
| FRotator | **[[AimRotation]]**  |
| TMap< FName, FName > | **[[AltCombatStates]]**  |
| TMap< FName, FName > | **[[AltDeflectSections]]**  |
| TMap< FName, FName > | **[[AltFeintToParrySections]]**  |
| TMap< FName, FName > | **[[AltParryStartSections]]**  |
| TMap< FName, FName > | **[[AltParrySuccessSections]]**  |
| EAnimGraphBranch01 | **[[AnimGraphBranch01]]**  |
| [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * | **[[AnimationSetBase]]**  |
| [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * | **[[AnimationSetBase1P]]**  |
| [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * | **[[AnimationSetBase3P]]**  |
| [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * | **[[AnimationSetBaseDeath]]**  |
| [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * | **[[AnimationSetBaseMount]]**  |
| [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * | **[[AnimationSetBaseSiege]]**  |
| TSubclassOf< [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) > | **[[AnimationSetDeath1P_Default]]**  |
| TSubclassOf< [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) > | **[[AnimationSetDeath3P_Default]]**  |
| TSubclassOf< [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) > | **[[AnimationSetMount_Class_Default]]**  |
| FName | **[[AnimationSetName]]**  |
| FName | **[[AnimationSetName_OffHand]]**  |
| TSubclassOf< [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) > | **[[AnimationSetOffhand1P_Class_Default]]**  |
| TSubclassOf< [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) > | **[[AnimationSetOffhand3P_Class_Default]]**  |
| TSubclassOf< [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) > | **[[AnimationSetPeasant_Class_Default]]**  |
| TSubclassOf< [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) > | **[[AnimationSetSiege_Class_Default]]**  |
| TArray< FName > | **[[AttackStates]]**  |
| [UAttackType](/docs/SDK/Source/Classes/classUAttackType.md) * | **[[AttackType]]**  |
| float | **[[AttackWindupWeight]]**  |
| [UTBLBatteringRamAnimInstance](/docs/SDK/Source/Classes/classUTBLBatteringRamAnimInstance.md) * | **[[BatteringRamAnimBP]]**  |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[CarryableParentCharacter]]**  |
| [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * | **[[CharAnimationSet]]**  |
| [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * | **[[CharAnimationSet1P]]**  |
| [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * | **[[CharAnimationSet3P]]**  |
| [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * | **[[CharAnimationSetDeath]]**  |
| [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * | **[[CharAnimationSetMount]]**  |
| [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * | **[[CharAnimationSetOffHand]]**  |
| [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * | **[[CharAnimationSetOffHand1P]]**  |
| [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * | **[[CharAnimationSetOffHand3P]]**  |
| [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * | **[[CharAnimationSetPeasant]]**  |
| [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * | **[[CharAnimationSetSiege]]**  |
| float | **[[CharMoveWeight]]**  |
| [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * | **[[CharPreviousAnimationSet]]**  |
| FName | **[[CombatState]]**  |
| [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * | **[[CombatStateBlueprint]]**  |
| float | **[[CombatStatePercent]]**  |
| UDataTable * | **[[ComboBlendTimeDataTable]]**  |
| TMap< [FComboMontageRule](/docs/SDK/Source/Classes/structFComboMontageRule.md), FName > | **[[ComboMontageRules]]**  |
| FName | **[[ComboState]]**  |
| [FAttackMontage](/docs/SDK/Source/Classes/structFAttackMontage.md) | **[[CurrentAttackMontage]]**  |
| [FCombatStateMontage](/docs/SDK/Source/Classes/structFCombatStateMontage.md) | **[[CurrentCombatStateMontage]]**  |
| FName | **[[CurrentEmoteMontageName]]**  |
| FName | **[[CurrentEmoteName]]**  |
| float | **[[CurrentSpeed]]**  |
| float | **[[CurrentSpeed2d]]**  |
| float | **[[DashDirection]]**  |
| TMap< FName, FName > | **[[DeflectSections]]**  |
| TMap< FName, float > | **[[DelayBackToIdle]]**  |
| TMap< FName, FName > | **[[DownedKnockdownSections]]**  |
| TMap< FName, FName > | **[[DownedPickupSections]]**  |
| TMap< FName, FName > | **[[DownedStaggerSections]]**  |
| TMap< FName, FName > | **[[FallingGetUpSections]]**  |
| UAnimMontage * | **[[FallingMontage]]**  |
| TMap< FName, FName > | **[[FallingSections]]**  |
| TMap< FName, FName > | **[[FeintMontage]]**  |
| TMap< FName, FName > | **[[FeintToParrySections]]**  |
| [FFootStepSounds](/docs/SDK/Source/Classes/structFFootStepSounds.md) | **[[FootStepSounds]]**  |
| TMap< FName, FName > | **[[GetUpSections]]**  |
| TMap< FName, FName > | **[[HeavyAttacks]]**  |
| TArray< FName > | **[[HideServerBones]]**  |
| [AHorse](/docs/SDK/Source/Classes/classAHorse.md) * | **[[Horse]]**  |
| [UTBLHorseAnimInstance](/docs/SDK/Source/Classes/classUTBLHorseAnimInstance.md) * | **[[HorseAnimBP]]**  |
| float | **[[IdlePoseStateTime]]**  |
| int32 | **[[Index_LOD]]**  |
| float | **[[InitialMoveTime]]**  |
| FVector | **[[InputDir]]**  |
| UAnimMontage * | **[[InteractMontage]]**  |
| float | **[[InventoryAnimationLength]]**  |
| bool | **[[Is3p]]**  |
| bool | **[[IsAltPosition]]**  |
| bool | **[[IsAttackQueued]]**  |
| bool | **[[IsCrouch]]**  |
| bool | **[[IsCustomizationAnimInstance]]**  |
| bool | **[[IsDead]]**  |
| bool | **[[IsDowned]]**  |
| bool | **[[IsItemEquipped]]**  |
| bool | **[[IsLeftFootTap]]**  |
| bool | **[[IsLunge]]**  |
| bool | **[[IsMove]]**  |
| bool | **[[IsOffHandAttack]]**  |
| bool | **[[IsOnHorse]]**  |
| bool | **[[IsOnSiege]]**  |
| bool | **[[IsPostInitialized]]**  |
| bool | **[[IsRagdoll]]**  |
| bool | **[[IsRightFootTap]]**  |
| bool | **[[IsServer]]**  |
| bool | **[[IsShieldEquipped]]**  |
| FName | **[[JabDeflectSection]]**  |
| FName | **[[KnockdownDirection]]**  |
| TMap< FName, FName > | **[[KnockdownGroundSections]]**  |
| UAnimMontage * | **[[KnockdownMontage]]**  |
| TMap< FName, FName > | **[[KnockdownSections]]**  |
| FName | **[[LastMissingLimb]]**  |
| UAnimMontage * | **[[LastSpawnMontage]]**  |
| FName | **[[LastSpawnSectionName]]**  |
| float | **[[LipSyncVOMeter]]**  |
| float | **[[LungeStartTime]]**  |
| float | **[[MaxSpeed]]**  |
| float | **[[MaxSpeedInCurrentState]]**  |
| TMap< EConditionType, FName > | **[[MissingLimbNames]]**  |
| TMap< FName, FName > | **[[MountCombatStates]]**  |
| TMap< FName, FName > | **[[MountDownSections]]**  |
| TMap< FName, FName > | **[[MountStaggerMontages]]**  |
| TMap< FName, FName > | **[[MountUpSections]]**  |
| float | **[[MovementDirection]]**  |
| int32 | **[[MovementDirectionIndex]]**  |
| float | **[[MovementDirectionTime]]**  |
| FName | **[[MovementState]]**  |
| float | **[[MovementStateInterpSpeed]]**  |
| float | **[[MovementStateWeight]]**  |
| TMap< UAnimMontage *, UAnimMontage * > | **[[NoBlend1PMontages]]**  |
| FAnimNotifyStepEvent | **[[OnAnimNotifyStepEvent]]**  |
| FAnimNotifyWeaponAttach | **[[OnAnimNotifyUseItem]]**  |
| FAnimNotifyWeaponAttach | **[[OnAnimNotifyWeaponAttach]]**  |
| FAnimNotifyWeaponAttach | **[[OnAnimNotifyWeaponDetach]]**  |
| FOnLadderAnimationEnded | **[[OnLadderAnimationEnded]]**  |
| bool | **[[OnStrafeStopNeedsEvent]]**  |
| UAnimMontage * | **[[ParryEventMontage]]**  |
| UAnimMontage * | **[[ParryMontage]]**  |
| UAnimMontage * | **[[ParryRiposteShieldMontage]]**  |
| TMap< FName, FName > | **[[ParryStartSections]]**  |
| UAnimMontage * | **[[ParrySuccessMontage]]**  |
| TMap< FName, FName > | **[[ParrySuccessSections]]**  |
| UAnimMontage * | **[[PeasantMontage]]**  |
| TMap< FName, [FPeasantMontage](/docs/SDK/Source/Classes/structFPeasantMontage.md) > | **[[PeasantStates]]**  |
| [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) * | **[[PreviousAnimationSetBase]]**  |
| [FAnimDamageParams](/docs/SDK/Source/Classes/structFAnimDamageParams.md) | **[[PreviousDamageParams]]**  |
| bool | **[[PreviousIsOnHorse]]**  |
| FVector | **[[PreviousMeshLocation]]**  |
| FName | **[[PreviousMovementState]]**  |
| FVector | **[[PreviousVelocity]]**  |
| UAnimMontage * | **[[ReloadMontage]]**  |
| TMap< [FComboMontageRule](/docs/SDK/Source/Classes/structFComboMontageRule.md), FName > | **[[RiposteMontageRules]]**  |
| TMap< FName, FName > | **[[SectionToCombatState]]**  |
| TArray< FName > | **[[ServerIdlePoseCombatStates]]**  |
| TArray< FName > | **[[ServerIdlePoseMovementStates]]**  |
| AActor * | **[[Siege]]**  |
| [UTBLAnimInstance](/docs/SDK/Source/Classes/classUTBLAnimInstance.md) * | **[[SiegeAnimBP]]**  |
| FName | **[[SiegeName]]**  |
| ECharacterSignificanceLevel | **[[SignificanceLevel]]**  |
| FName | **[[Socket_LeftStirrup]]**  |
| FName | **[[Socket_RightStirrup]]**  |
| float | **[[SpawnAnimStartTime]]**  |
| float | **[[SpeedLine]]**  |
| float | **[[SprintTurnAngle]]**  |
| FRotator | **[[SprintTurnDirection]]**  |
| float | **[[SprintTurnEndTime]]**  |
| float | **[[SprintTurnWeight]]**  |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[TBLCharacter]]**  |
| TMap< FName, FName > | **[[ThwackComboMontage]]**  |
| TMap< [FComboMontageRule](/docs/SDK/Source/Classes/structFComboMontageRule.md), FName > | **[[ThwackComboMontageRules]]**  |
| UCurveFloat * | **[[ThwackPlayRateCurve]]**  |
| FVector | **[[Velocity]]**  |
| float | **[[VelocityInterpSpeed]]**  |
| bool | **[[WasRecentlyRendered]]**  |
| bool | **[[bCarryablePickup]]**  |
| bool | **[[bIdlePoseCombatState]]**  |
| bool | **[[bIdlePoseMovementState]]**  |
| bool | **[[bIsPlayingSequencerAnimation]]**  |
| [UTBLCharacterMovement](/docs/SDK/Source/Classes/classUTBLCharacterMovement.md) * | **[[movement]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200