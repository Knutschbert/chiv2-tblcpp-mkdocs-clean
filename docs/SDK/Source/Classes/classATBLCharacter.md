---
title: ATBLCharacter
type: class
aliases: ATBLCharacter
share: false

---

# ATBLCharacter





Inherits from [ATBLCharacterBase](/docs/SDK/Source/Classes/classATBLCharacterBase.md), IVisualLoggerDebugSnapshotInterface, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md), IGenericTeamAgentInterface, [IMatchStateListenerInterface](/docs/SDK/Source/Classes/classIMatchStateListenerInterface.md), IAISightTargetInterface, [ISignificanceInterface](/docs/SDK/Source/Classes/classISignificanceInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ATBLCharacter]]**() |
| void | **[[AddConstructableActor]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * CarryableItem, AActor * NewActor) |
| void | **[[BroadcastCharacterEmote]]**(uint8 EmoteRowNum, EAudioPersonalityType::Type PersonalityType, uint8 EmotePlayingSeqNum, uint8 EmoteRandomSeed, uint8 bIsOverrideEmote, uint8 EmoteType) |
| void | **[[BroadcastChickenEmote]]**() |
| void | **[[BroadcastCinematicAllowControl]]**() |
| void | **[[BroadcastCinematicRestrictControl]]**() |
| void | **[[BroadcastClashEvent]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Target, [FClashEventReplicated](/docs/SDK/Source/Classes/structFClashEventReplicated.md) ClashEventReplicated) |
| void | **[[BroadcastDetachFromController]]**() |
| void | **[[BroadcastHitWorld]]**(const [FHitWorldParams](/docs/SDK/Source/Classes/structFHitWorldParams.md) & Params) |
| void | **[[BroadcastLoseHelmet]]**() |
| void | **[[BroadcastOnHealedByLocalPlayer]]**() |
| void | **[[BroadcastParryEvent]]**(AActor * Target, [FParryEventReplicated](/docs/SDK/Source/Classes/structFParryEventReplicated.md) ParryEventReplicated) |
| bool | **[[CanClash]]**() const |
| bool | **[[CanFullSprint]]**() const |
| bool | **[[CanSprintAttack]]**() const |
| bool | **[[CanSprintCharge]]**() const |
| bool | **[[CanSprintShove]]**() const |
| void | **[[CarryableAnimationEvent]]**(FName EventName) |
| void | **[[CarryableCharacterEvent]]**(FName EventName, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * ParentCharacter) |
| void | **[[ClearTutorialPlayerControl]]**() |
| void | **[[ClientApplyCondition]]**(EConditionType Condition) |
| void | **[[ClientDrawDebugArrow]]**(FVector LineStart, FVector LineEnd, FColor Clr, bool bPersistentLines, float Lifetime, float Thickness) |
| void | **[[ClientDrawDebugBox]]**(FVector Center, FVector Box, FTransform Transform, FColor Color, bool bPersistentLines, float Lifetime) |
| void | **[[ClientDrawDebugCapsule]]**(FVector Center, float HalfHeight, float Radius, FColor Color) |
| void | **[[ClientDrawDebugLine]]**(FVector LineStart, FVector LineEnd, FColor Clr, bool bPersistentLines, float Lifetime, float Thickness) |
| void | **[[ClientDrawDebugPoint]]**(FVector Location, float Size, FColor Clr, bool bPersistentLines, float Lifetime) |
| void | **[[ClientDrawDebugPose]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character, FColor Clr) |
| void | **[[ClientDrawDebugSphere]]**(FVector Center, float Radius, int32 Segments, FColor Clr, bool bPersistentLines) |
| void | **[[ClientDrawDebugString]]**(FVector Location, const FString & Text, FColor Clr, float Duration, float FontScale) |
| void | **[[ClientReliableNotifySuicide]]**(EKillReason KillReason) |
| void | **[[ClientSetCustomizationSwatches]]**(const TArray< [FSwatchSelection](/docs/SDK/Source/Classes/structFSwatchSelection.md) > & Swatches) |
| void | **[[ClientSuicideReceived]]**([FDamageTakenEventCompressed](/docs/SDK/Source/Classes/structFDamageTakenEventCompressed.md) DamageEventCompressed) |
| void | **[[ClientTeleportTo]]**(FVector vecTargetPos, FRotator vecTargetRot) |
| void | **[[ConditionAppliedByActor]]**(EConditionType ConditionApplied, AActor * ConditionCauser) |
| void | **[[ConsumeInputAction]]**(FName ActionName, TEnumAsByte< EInputEvent > InputType) |
| void | **[[DamageWithHitParams]]**(float Damage, FHitResult HitResult, FVector HitDirection, bool bLoseLimbCheat) |
| void | **[[DebugDrawCamera]]**(float DeltaTime) |
| void | **[[DebugDrawParryBox]]**(float DeltaTime) |
| void | **[[DebugDrawShield]]**([ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * DebugController) |
| void | **[[DoKeyAxis]]**(FName ActionName, float AxisValue) |
| void | **[[DoKeyEvent]]**(FName ActionName, TEnumAsByte< EInputEvent > KeyEvent) |
| bool | **[[DoesCountTowardKillsAndKnockdowns]]**() const |
| TArray< AActor * > | **[[GetAIObjectiveActors]]**() const |
| FString | **[[GetAIObjectiveDebugString]]**() |
| void | **[[GetActionEvent]]**(UAkAudioEvent *& StartEvent, UAkAudioEvent *& StopEvent) |
| AActor * | **[[GetActorWhoAppliedCondition]]**(EConditionType ConditionApplied) |
| float | **[[GetAnimationPercent]]**() const |
| float | **[[GetAutoVODistanceSqrdByType]]**(TEnumAsByte< EAudioAutoVOType::Type > Type) |
| void | **[[GetBattlecryActionEvent]]**(UAkAudioEvent *& StartEvent, UAkAudioEvent *& StopEvent) |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[GetBlockingInventoryItem]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * AttackingCharacter) const |
| FVector | **[[GetCameraSocketLocation]]**() const |
| FVector | **[[GetCenterPlayArea]]**() const |
| TEnumAsByte< EAudioClassType::Type > | **[[GetCharacterAudioType]]**() const |
| ECharacterClass | **[[GetCharacterClassArchetype]]**(ECharacterClass Type) |
| FString | **[[GetCharacterClassAudioSwitch]]**(TEnumAsByte< EAudioClassType::Type > ClassType, EFaction Faction) |
| ECharacterClassType | **[[GetCharacterClassType]]**(ECharacterClass Type) |
| [UCombatStateComponent](/docs/SDK/Source/Classes/classUCombatStateComponent.md) * | **[[GetCombatStateComponent]]**() const |
| TArray< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * > | **[[GetCurrentAttackingWeapons]]**() const |
| USkeletalMeshComponent * | **[[GetCurrentMesh]]**() const |
| float | **[[GetDeathTime]]**() |
| TArray< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * > | **[[GetEquippedInventoryItems]]**() const |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[GetEquippedItemByHand]]**(EEquippedHand Hand) const |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[GetEquippedWeapon]]**() const |
| FVector | **[[GetFacingDirection]]**() const |
| [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * | **[[GetFocusedInteractable]]**() |
| [UInventory](/docs/SDK/Source/Classes/classUInventory.md) * | **[[GetInventory]]**() const |
| AController * | **[[GetLastController]]**() |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| float | **[[GetNeedsHealingThreshold]]**() |
| TArray< [UParryComponent](/docs/SDK/Source/Classes/classUParryComponent.md) * > | **[[GetParryComponents]]**() |
| ECharacterClass | **[[GetPawnClassArchetype]]**() const |
| ECharacterClass | **[[GetPawnClassType]]**() const |
| USkeletalMeshComponent * | **[[GetPawnMesh]]**(bool WantFirstPerson) const |
| TEnumAsByte< EAudioPersonalityType::Type > | **[[GetPersonalityType]]**() const |
| [USpecialItemAbility](/docs/SDK/Source/Classes/classUSpecialItemAbility.md) * | **[[GetSpecialItemAbility]]**() |
| [FThirdPersonCameraParams](/docs/SDK/Source/Classes/structFThirdPersonCameraParams.md) | **[[GetThirdPersonCameraParams]]**() |
| void | **[[HandleOnCustomizationJobsEmptied]]**() |
| bool | **[[HasCondition]]**(EConditionType Condition) const |
| void | **[[HideCharacterAndEquipment]]**(bool bHide) |
| void | **[[HitClash]]**(FHitResult & Hit, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * OtherCharacter) |
| void | **[[HitWorld]]**(const FHitResult & Hit) |
| void | **[[HitWorldWithStats]]**(FHitResult Hit, bool bParried) |
| void | **[[InitiateAbilityByName]]**(FName AbilityName) |
| void | **[[InterruptUse]]**(FName NextCombatState) |
| bool | **[[IsArrowCameraEnabled]]**() const |
| bool | **[[IsBlocking]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * AttackingCharacter) const |
| bool | **[[IsCharacterClassArchetype]]**(ECharacterClass Type) |
| bool | **[[IsCharacterPaused]]**() const |
| bool | **[[IsCinematicRestrictedControl]]**() |
| bool | **[[IsFacingTarget]]**(const FHitResult & Hit, const [FFacingTargetParams](/docs/SDK/Source/Classes/structFFacingTargetParams.md) & Params) |
| bool | **[[IsFollowAnimationEnabled]]**() const |
| bool | **[[IsHoldingAltAttack]]**(float Tolerance) |
| bool | **[[IsInParryView]]**([UParryComponent](/docs/SDK/Source/Classes/classUParryComponent.md) * ParryComp, const FTransform & BoxTransform, const FVector & BoxExtents, float IgnoreParryDepth) const |
| bool | **[[IsInRagdoll]]**() const |
| bool | **[[IsInitialAutorun]]**() const |
| bool | **[[IsInterpingToMountLocation]]**() const |
| bool | **[[IsLocalPlayer]]**() |
| bool | **[[IsPawnSubclass]]**() const |
| bool | **[[IsSpawnFadeOutEnabled]]**() const |
| bool | **[[IsSpecialPawnClass]]**() const |
| bool | **[[IsSprinting]]**() |
| void | **[[Kill]]**(EKillReason KillReason, bool bSwitchedTeamsInLoadoutVolume, AActor * Killer) |
| void | **[[KillWithHitParams]]**(EKillReason KillReason, bool bSwitchedTeamsInLoadoutVolume, FHitResult HitResult, FVector HitDirection, AActor * Killer) |
| void | **[[LoserEnterPostGameState]]**() |
| void | **[[NetMulticastFastSharedReplication]]**(const [FFastSharedProperties_TBLCharacter](/docs/SDK/Source/Classes/structFFastSharedProperties__TBLCharacter.md) & Properties) |
| void | **[[OnAttachedRagdollActorDestroyed]]**(AActor * DestroyedActor) |
| void | **[[OnCombatStateBegin]]**(AActor * Actor, FName State, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * CombatState) |
| void | **[[OnCombatStateEnd]]**(AActor * Actor, FName State, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * CombatState) |
| void | **[[OnCustomized]]**() |
| void | **[[OnInitializeAltWeightsState]]**() |
| void | **[[OnMeleeHitSuccess]]**(AActor * HitActor) |
| void | **[[OnRep_AttachToProjectile]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Projectile) |
| void | **[[OnRep_BeingRevivedBy]]**() |
| void | **[[OnRep_InventorySlots]]**() |
| void | **[[OnRep_LockMeshRotation]]**() |
| void | **[[OnRep_ShouldCharacterBeHidden]]**() |
| void | **[[OnRep_SpawnedAtSpawnComp]]**() |
| void | **[[OnRep_SpecialItemCharge]]**() |
| void | **[[PauseCharacter]]**(bool bPaused) |
| void | **[[PlayAutoVO]]**(TEnumAsByte< EAudioAutoVOType::Type > AutoVoType) |
| void | **[[PlayAutoVOFromServer]]**(TEnumAsByte< EAudioAutoVOType::Type > AutoVoType, bool SkipLocalPlayer) |
| void | **[[PlayCharacterActionEvent]]**(const [FSoundSwitchEntry](/docs/SDK/Source/Classes/structFSoundSwitchEntry.md) SoundSwitch, bool IsLocalPlayerInvolved) const |
| void | **[[PlayChickenEmote]]**() |
| bool | **[[PlayEmote]]**([FPersonalityEmoteTableRow](/docs/SDK/Source/Classes/structFPersonalityEmoteTableRow.md) Emote, ERadialVOMenuPage Page) |
| void | **[[PlayEmoteFromServer]]**(FName EmoteName) |
| void | **[[PlayHighPriorityCharacterActionEvent]]**(const [FSoundSwitchEntry](/docs/SDK/Source/Classes/structFSoundSwitchEntry.md) SoundSwitch) |
| void | **[[PlayLowPriorityCharacterActionEvent]]**(const [FSoundSwitchEntry](/docs/SDK/Source/Classes/structFSoundSwitchEntry.md) SoundSwitch) const |
| void | **[[PushRespawnState]]**() |
| void | **[[RemoveEmoteFromQueue]]**(int32 EmoteId) |
| void | **[[Revive]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * DownedCharacter) |
| void | **[[ServerEnterPostGameState]]**() |
| void | **[[ServerHandleOnCustomizationJobsEmptied]]**() |
| void | **[[ServerHitWorld]]**(const [FHitWorldParams](/docs/SDK/Source/Classes/structFHitWorldParams.md) & Params, float ClientTimeStamp) |
| void | **[[ServerPlayChickenEmote]]**() |
| void | **[[ServerPlayEmote]]**(uint8 EmoteRowNum, EAudioPersonalityType::Type PersonalityType, uint8 EmotePlayingSeqNum, uint8 bIsOverrideEmote, uint8 EmoteType) |
| void | **[[SetCinematicRestrictedControl]]**(bool bRestricted) |
| void | **[[SetDeathAnimationParameters]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & Event) |
| void | **[[SetFirstPersonDeathCamera]]**() |
| void | **[[SetIgnoreAI]]**(bool bNewIgnoreAI) |
| void | **[[SetIsInitialAutorun]]**() |
| void | **[[SetPlayerDrunk]]**(bool IsDrunk) |
| void | **[[SetRagdollPhysics]]**() |
| void | **[[SetSpectatingPawn]]**([ATBLSpectatorPawn](/docs/SDK/Source/Classes/classATBLSpectatorPawn.md) * NewSpectatingPawn) |
| void | **[[SetThirdPersonDeathCamera]]**() |
| void | **[[SetupAI]]**() |
| bool | **[[ShouldAttackBeCountered]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * AttackingCharacter, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * AttackingItem, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * DefenderItem) const |
| bool | **[[ShouldBlockCharacter]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * AttackingCharacter, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * HitCharacter, [FActionContext](/docs/SDK/Source/Classes/structFActionContext.md) & Context) const |
| bool | **[[ShouldClash]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * InitiatorCharacter, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * TargetCharacter, FVector ClashLocation) const |
| bool | **[[ShouldIgnoreAI]]**() const |
| void | **[[StartRevive]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * DownedCharacter) |
| void | **[[StopCharacterActionEvent]]**() |
| void | **[[StopHighPriorityCharacterActionEvent]]**() |
| void | **[[StopLowPriorityCharacterActionEvent]]**() |
| void | **[[StopRevive]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * DownedCharacter) |
| void | **[[Suicide]]**(EKillReason KillReason) |
| void | **[[SwitchAttachedItemMesh]]**(USkeletalMeshComponent * ParentMesh) |
| void | **[[TutorialPlayerControl]]**([FTutorialPlayerControlParams](/docs/SDK/Source/Classes/structFTutorialPlayerControlParams.md) Params) |
| void | **[[UnfreezeRagdoll]]**() |
| void | **[[UpdateLockMeshRotation]]**() |
| void | **[[UpdateRagdoll]]**(float DeltaSeconds) |
| void | **[[UpdateSpecialItemAbility]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * SpecialItem) |
| void | **[[UpdateThirdPersonCamera]]**(float DeltaSeconds, bool bSpectator) |
| void | **[[WasHitAfterDeath]]**(FHitResult & Hit, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * OtherCharacter) |
| void | **[[WasHitEarly]]**(const FHitResult & Hit, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * AttackingCharacter) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AddConstructableActorToArray]]**(AActor * NewActor) |
| void | **[[BroadcastAbleToHealIfChanged]]**() |
| void | **[[BroadcastHitWorldWithStats]]**(const [FHitWorldParams](/docs/SDK/Source/Classes/structFHitWorldParams.md) & Params) |
| void | **[[BroadcastPauseCharacter]]**(bool bPaused) |
| void | **[[BroadcastWasHitEarly]]**(const [FEarlyHitResult](/docs/SDK/Source/Classes/structFEarlyHitResult.md) & EarlyHit) |
| bool | **[[CanRevive]]**(APawn * Pawn) |
| void | **[[CheckTeamCollision]]**(AActor * OtherActor, UPrimitiveComponent * OtherComp) |
| void | **[[DeathAnimationOverlap]]**() |
| void | **[[FellOutOfWorldTimer]]**() |
| void | **[[OnApplyCondition]]**(AActor * Actor, EConditionType Condition) |
| void | **[[OnCausedDamage]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & DamageEvent) |
| void | **[[OnComponentHit]]**(UPrimitiveComponent * HitComponent, AActor * OtherActor, UPrimitiveComponent * OtherComp, FVector NormalImpulse, const FHitResult & Hit) |
| void | **[[OnComponentOverlap]]**(UPrimitiveComponent * OverlappedComponent, AActor * Other, UPrimitiveComponent * OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult & OverlapInfo) |
| void | **[[OnConstructableActorDestroyed]]**(AActor * DestroyedActor) |
| void | **[[OnConstructableActorKilled]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & Event) |
| void | **[[OnDamageTaken]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & DamageEvent) |
| void | **[[OnEquippedItemsChanged]]**() |
| void | **[[OnInteractableUsePawnChanged]]**(APawn * Pawn) |
| void | **[[OnKilled]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & DamageEvent) |
| void | **[[OnProjectileStopAfterDeath]]**(const FHitResult & ImpactResult) |
| void | **[[OnRep_CinematicRestrictedControl]]**() |
| void | **[[OnRep_RandomSeed]]**(int32 PreviousRandomInt) |
| void | **[[OnTeamChanged]]**([ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * OwnerTeam) |
| void | **[[ProcessTurnAndLookInput]]**(const TEnumAsByte< EAxis::Type > Axis, const float Value) |
| void | **[[ProcessTurnAndLookInputRate]]**(const TEnumAsByte< EAxis::Type > Axis, const float Rate) |
| void | **[[RemoveConstructableActor]]**(AActor * DestroyedActor) |
| void | **[[ServerDismountPressed]]**() |
| void | **[[ServerSetFireSource]]**([UFireSourceComponent](/docs/SDK/Source/Classes/classUFireSourceComponent.md) * NewFireSource) |
| void | **[[ServerUse]]**([UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * Interactable, bool bIsAutoPickup) |
| void | **[[ServerUseHeldComplete]]**([UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * Interactable) |
| void | **[[ServerUseHeldRelease]]**([UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * Interactable) |
| void | **[[ServerUseHeldStart]]**([UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * Interactable) |
| void | **[[ServerUseTornOffItem]]**(TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > ItemClass, FName TornOffName) |
| void | **[[UpdateAttachedSmoothing]]**(float DeltaSeconds) |
| void | **[[UpdateBlending]]**(float DeltaSeconds) |
| void | **[[UpdateParryAim]]**(float DeltaSeconds) |
| void | **[[UpdatePlayingVO]]**(float DeltaSeconds) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [UAbilitiesComponent](/docs/SDK/Source/Classes/classUAbilitiesComponent.md) * | **[[Abilities]]**  |
| TMap< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) *, [FArmHitInfo](/docs/SDK/Source/Classes/structFArmHitInfo.md) > | **[[ArmHits]]**  |
| [FAttachRagdollBlendParams](/docs/SDK/Source/Classes/structFAttachRagdollBlendParams.md) | **[[AttachRagdollBlendParams]]**  |
| TArray< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * > | **[[AttachedItems]]**  |
| [FAttachedRagdoll](/docs/SDK/Source/Classes/structFAttachedRagdoll.md) | **[[AttachedRagdoll]]**  |
| float | **[[AttackFromBehindAngle]]**  |
| TEnumAsByte< EAudioClassType::Type > | **[[AudioClassType]]**  |
| TArray< [UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * > | **[[AutoVONegativeDamageSources]]**  |
| TMap< TEnumAsByte< EAudioAutoVOType::Type >, float > | **[[AutoVOProbabilty]]**  |
| float | **[[BaseLookUpRate]]**  |
| float | **[[BaseTurnRate]]**  |
| UCameraComponent * | **[[Camera1P]]**  |
| [FCamera1PBlendParams](/docs/SDK/Source/Classes/structFCamera1PBlendParams.md) | **[[Camera1PBlendParams]]**  |
| FName | **[[Camera1PSocket]]**  |
| UCameraComponent * | **[[Camera3P]]**  |
| FName | **[[Camera3PSocket]]**  |
| FVector | **[[CameraOffset1P]]**  |
| TArray< TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > > | **[[CharacterSubclasses]]**  |
| [UProgressionSpec](/docs/SDK/Source/Classes/classUProgressionSpec.md) * | **[[ClassProgressionSpec]]**  |
| TArray< FName > | **[[ClientTracerHitBones]]**  |
| TArray< TWeakObjectPtr< UPrimitiveComponent > > | **[[ClientTracerHitComponents]]**  |
| int32 | **[[ClientTracerHitCount]]**  |
| [UCombatStateComponent](/docs/SDK/Source/Classes/classUCombatStateComponent.md) * | **[[CombatStateComponent]]**  |
| [UCombatStateQueue](/docs/SDK/Source/Classes/classUCombatStateQueue.md) * | **[[CombatStateQueue]]**  |
| TSubclassOf< [UCombatStateSet](/docs/SDK/Source/Classes/classUCombatStateSet.md) > | **[[CombatStateSet]]**  |
| [UCombatStateSynchronization](/docs/SDK/Source/Classes/classUCombatStateSynchronization.md) * | **[[CombatStateSynchronization]]**  |
| [UConditionsComponent](/docs/SDK/Source/Classes/classUConditionsComponent.md) * | **[[ConditionsComponent]]**  |
| [FThirdPersonCameraParams](/docs/SDK/Source/Classes/structFThirdPersonCameraParams.md) | **[[CurrentCameraParams]]**  |
| [UCustomizationComponent](/docs/SDK/Source/Classes/classUCustomizationComponent.md) * | **[[CustomizationComponent]]**  |
| [FCustomizationContext](/docs/SDK/Source/Classes/structFCustomizationContext.md) | **[[CustomizationContext]]**  |
| uint8 | **[[DeadCharacterId]]**  |
| FName | **[[DeathAnimationMontageName]]**  |
| FName | **[[DeathAnimationSectionName1p]]**  |
| FName | **[[DeathAnimationSectionName3p]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[DebugDroppedItem]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[DebugFakeClientProjectile]]**  |
| [FDebugMovementReplication](/docs/SDK/Source/Classes/structFDebugMovementReplication.md) | **[[DebugMovementReplication]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[DebugProjectile]]**  |
| USkeletalMesh * | **[[DefaultMesh1P]]**  |
| [FCharacterDisplayInfo](/docs/SDK/Source/Classes/structFCharacterDisplayInfo.md) | **[[DisplayInfo]]**  |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[EquippedCarryableOnSpawn]]**  |
| float | **[[FirstPossessedTimeSeconds]]**  |
| [UFollowMasterSkeletalMeshComponent](/docs/SDK/Source/Classes/classUFollowMasterSkeletalMeshComponent.md) * | **[[FollowMeshComponent]]**  |
| int32 | **[[GamepadUsePressedCount]]**  |
| float | **[[GamepadUsePressedStartTime]]**  |
| FRotator | **[[GoreHeadRotationOffset]]**  |
| TArray< AActor * > | **[[HeadShotActors]]**  |
| [UHeadlookComponent](/docs/SDK/Source/Classes/classUHeadlookComponent.md) * | **[[HeadlookComponent]]**  |
| TArray< TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > > | **[[HealingItemTypes]]**  |
| TArray< TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > > | **[[HealingSpecialItemTypes]]**  |
| TArray< [FHitActorWithItemInfo](/docs/SDK/Source/Classes/structFHitActorWithItemInfo.md) > | **[[HitActorWithWeaponInfos]]**  |
| [FHorseLookAtParams](/docs/SDK/Source/Classes/structFHorseLookAtParams.md) | **[[HorseLookAtParams]]**  |
| [FHorseLookAtParams](/docs/SDK/Source/Classes/structFHorseLookAtParams.md) | **[[HorseOrientCameraOnBumpParams]]**  |
| [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * | **[[InteractableComponent]]**  |
| [AHorse](/docs/SDK/Source/Classes/classAHorse.md) * | **[[KnockdownOffHorse]]**  |
| TWeakObjectPtr< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > | **[[LastCharacterHitBy]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[LastFiredProjectile]]**  |
| [FParryEventState](/docs/SDK/Source/Classes/structFParryEventState.md) | **[[LastParryEvent]]**  |
| FBasedMovementInfo | **[[LastReplicatedBasedMovement]]**  |
| TWeakObjectPtr< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[LastWeaponHitBy]]**  |
| TSubclassOf< [ULoadoutSelection](/docs/SDK/Source/Classes/classULoadoutSelection.md) > | **[[LoadoutSelection]]**  |
| [FLockMeshBlendOutParams](/docs/SDK/Source/Classes/structFLockMeshBlendOutParams.md) | **[[LockMeshBlendInParams]]**  |
| [FLockMeshBlendOutParams](/docs/SDK/Source/Classes/structFLockMeshBlendOutParams.md) | **[[LockMeshBlendOutParams]]**  |
| USkeletalMeshComponent * | **[[Mesh1P]]**  |
| FVector | **[[Mesh1PLocation]]**  |
| FRotator | **[[Mesh1PRotation]]**  |
| [FBlendParams](/docs/SDK/Source/Classes/structFBlendParams.md) | **[[MountControlBlendParams]]**  |
| float | **[[MountOrDismountCameraInterpSpeed]]**  |
| [FMountRootBlendParams](/docs/SDK/Source/Classes/structFMountRootBlendParams.md) | **[[MountRootBlendParams]]**  |
| [UMovementDebugger](/docs/SDK/Source/Classes/classUMovementDebugger.md) * | **[[MovementDebugger]]**  |
| [UMovementModifierComponent](/docs/SDK/Source/Classes/classUMovementModifierComponent.md) * | **[[MovementModifiers]]**  |
| float | **[[ObjectHighlightMaxDistance]]**  |
| FOnAbleToHealChanged | **[[OnAbleToHealChanged]]**  |
| FOnAnimationSetChanged | **[[OnAnimationSetChanged]]**  |
| FOnBeingRevivedByChangedSignature | **[[OnBeingRevivedByChangedDelegate]]**  |
| FOnCameraChanged | **[[OnCameraChanged]]**  |
| FOnCarryableAnimationEvent | **[[OnCarryableAnimationEvent]]**  |
| FOnCarryableCharacterEvent | **[[OnCarryableCharacterEvent]]**  |
| FCinematicAllowedControl | **[[OnCinematicAllowedControl]]**  |
| FCinematicRestrictedControl | **[[OnCinematicRestrictedControl]]**  |
| FOnClash | **[[OnClash]]**  |
| FOnClientNotifyKilled | **[[OnClientNotifyKilled]]**  |
| FOnClientNotifySuicide | **[[OnClientNotifySuicide]]**  |
| FOnDamageEvent | **[[OnDamage]]**  |
| FOnDamageEvent | **[[OnDamageCaused]]**  |
| FOnDismount | **[[OnDismount]]**  |
| FOnDismountPressed | **[[OnDismountPressed]]**  |
| FOnFallDamageEvent | **[[OnFallDamage]]**  |
| FOnFreezeRagdollPhysics | **[[OnFreezeRagdollPhysics]]**  |
| FOnHealedByLocalPlayer | **[[OnHealedByLocalPlayer]]**  |
| FOnHitWorld | **[[OnHitWorld]]**  |
| FOnInteractableFocused | **[[OnInteractableFocused]]**  |
| FOnInteractableLostFocus | **[[OnInteractableLostFocus]]**  |
| FInventoryItemEquipped | **[[OnInventoryItemEquipped]]**  |
| FInventoryItemEquipped | **[[OnInventoryItemToBeEquipped]]**  |
| FInventoryItemEquipped | **[[OnInventoryItemUnequipped]]**  |
| FOnMeleeSuccess | **[[OnMeleeSuccess]]**  |
| FOnMount | **[[OnMount]]**  |
| FOnParryEvent | **[[OnParrySuccess]]**  |
| FOnPlayEmote | **[[OnPlayEmote]]**  |
| FOnPlayerMeshChanged | **[[OnPlayerMeshChanged]]**  |
| FOnRepCharacterPlayerState | **[[OnPlayerStateReplicated]]**  |
| FOnPossessedSignature | **[[OnPossessed]]**  |
| FOnProjectileBeginPlay | **[[OnProjectileBeginPlay]]**  |
| FOnRootMotionChanged | **[[OnRootMotionChanged]]**  |
| FOnSetFirstPersonDeathCamera | **[[OnSetFirstPersonDeathCamera]]**  |
| FOnSetRagdollPhysics | **[[OnSetRagdollPhysics]]**  |
| FOnSetThirdPersonDeathCamera | **[[OnSetThirdPersonDeathCamera]]**  |
| FOnShowInGameMenuDelegate | **[[OnShowInGameMenu]]**  |
| FOnSpecialItemAbilitySet | **[[OnSpecialAbilitySet]]**  |
| FOnStaminaCostFailed | **[[OnStaminaCostFailed]]**  |
| FOnStartHeal | **[[OnStartHeal]]**  |
| FOnStatsComponentFocused | **[[OnStatsComponentFocused]]**  |
| FOnStatsComponentLostFocus | **[[OnStatsComponentLostFocused]]**  |
| FOnUnderCrosshairChanged | **[[OnUnderCrosshairChanged]]**  |
| FOnFreezeRagdollPhysics | **[[OnUnfreezeRagdollPhysics]]**  |
| FOnInteractableFocused | **[[OnUseableActorInteractableFocused]]**  |
| FOnInteractableFocused | **[[OnUseableActorInteractableLostFocused]]**  |
| FOnWasHitEarly | **[[OnWasHitEarly]]**  |
| FOnParryEvent | **[[OnWasParried]]**  |
| FName | **[[OnlineXpStatName]]**  |
| TSubclassOf< [ULoadoutSelection](/docs/SDK/Source/Classes/classULoadoutSelection.md) > | **[[OverrideLoadoutSelection]]**  |
| TMap< FSoftObjectPath, uint32 > | **[[ParticleSystemsToPrepopulate]]**  |
| ECharacterClass | **[[PawnClassType]]**  |
| [UPerksComponent](/docs/SDK/Source/Classes/classUPerksComponent.md) * | **[[PerksComponent]]**  |
| FPlayInventoryAnimation | **[[PlayInventoryAnimation]]**  |
| [FReplicationPredictionState](/docs/SDK/Source/Classes/structFReplicationPredictionState.md) | **[[PredictionState]]**  |
| [UPushingComponent](/docs/SDK/Source/Classes/classUPushingComponent.md) * | **[[PushingComponent]]**  |
| int32 | **[[RandomSeed]]**  |
| uint8 | **[[ReplicatedServerFrame]]**  |
| USkeletalMesh * | **[[SKMesh3P]]**  |
| FSetOnHorse | **[[SetOnHorse]]**  |
| USceneComponent * | **[[SpawnedAtSpawnComp]]**  |
| [ASpawner](/docs/SDK/Source/Classes/classASpawner.md) * | **[[SpawnedAtSpawner]]**  |
| int32 | **[[SpawnerPosition]]**  |
| [USpecialItemAbility](/docs/SDK/Source/Classes/classUSpecialItemAbility.md) * | **[[SpecialItemAbility]]**  |
| [ATBLSpectatorPawn](/docs/SDK/Source/Classes/classATBLSpectatorPawn.md) * | **[[SpectatingPawn]]**  |
| [UStatsComponent](/docs/SDK/Source/Classes/classUStatsComponent.md) * | **[[Stats]]**  |
| [FThirdPersonCameraParams](/docs/SDK/Source/Classes/structFThirdPersonCameraParams.md) | **[[ThirdPersonCameraParams]]**  |
| [FTutorialLocationBlendParams](/docs/SDK/Source/Classes/structFTutorialLocationBlendParams.md) | **[[TutorialLocationBlendParams]]**  |
| [FTutorialLookAtParams](/docs/SDK/Source/Classes/structFTutorialLookAtParams.md) | **[[TutorialLookAtParams]]**  |
| TArray< [UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * > | **[[VOFriendlyDamageSources]]**  |
| TWeakObjectPtr< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[WeaponAppliedBleed]]**  |
| uint8 | **[[bCustomizationMenuComponentsSpawned]]**  |
| bool | **[[bDebugIgnoreAI]]**  |
| bool | **[[bHasAltAttack]]**  |
| bool | **[[bHasAttackedSuccessfully]]**  |
| bool | **[[bHelmetKnockedOff]]**  |
| bool | **[[bIsCinematicsRelevant]]**  |
| uint8 | **[[bIsForCustomizationMenu]]**  |
| bool | **[[bLastAbleToHealCheck]]**  |
| bool | **[[bPlayerNeedsHealing]]**  |
| bool | **[[bPreventForwardSpawn]]**  |
| bool | **[[bShouldCrouchOverrideRecoveryAnimation]]**  |
| bool | **[[bShouldPlayDeathAnimation]]**  |
| uint8 | **[[bSpawnedGoreHead]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< TEnumAsByte< EAudioAutoVOType::Type > > | **[[AliveFriendlyAudoVO]]**  |
| [FAttachedSmoothing](/docs/SDK/Source/Classes/structFAttachedSmoothing.md) | **[[AttachedSmoothing]]**  |
| UAkComponent * | **[[AudioComponent]]**  |
| UBehaviorTree * | **[[AutoPossessAIBehaviorTree]]**  |
| EFaction | **[[AutoPossessAIFaction]]**  |
| TMap< TEnumAsByte< EAudioAutoVOType::Type >, float > | **[[AutoVODistanceByType]]**  |
| float | **[[BattleCryVOCooldown]]**  |
| [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * | **[[BeingRevivedBy]]**  |
| [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * | **[[CachedInteractableUseHeldComponent]]**  |
| TArray< [UParryComponent](/docs/SDK/Source/Classes/classUParryComponent.md) * > | **[[CachedParryComponents]]**  |
| FTransform | **[[Camera3PRotation]]**  |
| TWeakObjectPtr< [UTeamCapturePointComponent](/docs/SDK/Source/Classes/classUTeamCapturePointComponent.md) > | **[[CapturePoint]]**  |
| [UFireSourceComponent](/docs/SDK/Source/Classes/classUFireSourceComponent.md) * | **[[ClosestFireSource]]**  |
| [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * | **[[ClosestInteractable]]**  |
| [UStatsComponent](/docs/SDK/Source/Classes/classUStatsComponent.md) * | **[[ClosestStatsComponent]]**  |
| TMap< uint8, TWeakObjectPtr< AActor > > | **[[ConditionsAppliedByActor]]**  |
| TArray< AActor * > | **[[ConstructableActors]]**  |
| TEnumAsByte< EAudioAutoVOType::Type > | **[[CurrentAutoVo]]**  |
| float | **[[DeathAnimationLength]]**  |
| float | **[[DeathAnimationToRagdollImpulse]]**  |
| TArray< TEnumAsByte< EAudioAutoVOType::Type > > | **[[DeathFriendlyAudoVO]]**  |
| float | **[[DeathTime]]**  |
| float | **[[FellOutOfWorldKillTime]]**  |
| float | **[[GamepadDismountPressedStartTime]]**  |
| [FInteractableSettings](/docs/SDK/Source/Classes/structFInteractableSettings.md) | **[[InteractableSettings]]**  |
| [UInventory](/docs/SDK/Source/Classes/classUInventory.md) * | **[[Inventory]]**  |
| AController * | **[[LastController]]**  |
| [ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * | **[[LastPlayerController]]**  |
| [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * | **[[LastPlayerState]]**  |
| UCurveFloat * | **[[LipSyncVOCurve]]**  |
| float | **[[NeedsHealingThreshold]]**  |
| int32 | **[[NumberOfAllowedVOsWithinExpiry]]**  |
| TArray< float > | **[[PausedActorLifespans]]**  |
| TArray< AActor * > | **[[PausedActors]]**  |
| TArray< UActorComponent * > | **[[PausedComponents]]**  |
| TArray< UPrimitiveComponent * > | **[[PausedPhysics]]**  |
| TArray< FTimerHandle > | **[[PausedTimerHandles]]**  |
| bool | **[[PreviousIsPlayingRootMotion]]**  |
| [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * | **[[PreviousTeam]]**  |
| float | **[[RagdollStartTime]]**  |
| TMap< uint64, [FLastSightCheckInfo](/docs/SDK/Source/Classes/structFLastSightCheckInfo.md) > | **[[SightCacheMap]]**  |
| float | **[[TimeToVOExpiry]]**  |
| [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * | **[[UseableActorInteractable]]**  |
| float | **[[VOCooldown]]**  |
| float | **[[VOQueueEmoteWindow]]**  |
| [FVOTracker](/docs/SDK/Source/Classes/structFVOTracker.md) | **[[VOTracker]]**  |
| float | **[[WaitForAttachToProjectileTime]]**  |
| bool | **[[bAutoPossessAIStartCinematicRestricted]]**  |
| bool | **[[bCanSuicide]]**  |
| bool | **[[bCountTowardsKillsAndKnockdowns]]**  |
| bool | **[[bDidPushRespawnState]]**  |
| bool | **[[bHasRandomSeed]]**  |
| bool | **[[bIsCharacterPaused]]**  |
| uint8 | **[[bIsDying]]**  |
| bool | **[[bIsInitialAutorun]]**  |
| bool | **[[bNeverPerceiveCharacter]]**  |
| bool | **[[bPreventSuicide]]**  |
| bool | **[[bRagdollCustomTick]]**  |
| bool | **[[bRagdollTriggered]]**  |
| bool | **[[bRemovableBot]]**  |
| bool | **[[bSuicideTried]]**  |
| bool | **[[bTapOutHeld]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200