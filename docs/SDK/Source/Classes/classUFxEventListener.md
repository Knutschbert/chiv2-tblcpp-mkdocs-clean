---
title: UFxEventListener
type: class
aliases: UFxEventListener
share: false

---

# UFxEventListener





Inherits from [UTBLObject](/docs/SDK/Source/Classes/classUTBLObject.md), [UAssemblyObject](/docs/SDK/Source/Classes/classUAssemblyObject.md), UObject

Inherited by [UFxInstance](/docs/SDK/Source/Classes/classUFxInstance.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[OnAbilityError]]**(AActor * Initiator, EResultCode::Type Code, [AAbilityInvocation](/docs/SDK/Source/Classes/classAAbilityInvocation.md) * Invocation, FName AttackName, TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > ItemClass) |
| void | **[[OnAbilityOnCooldown]]**(const [FAbility](/docs/SDK/Source/Classes/structFAbility.md) & Ability, float RemainingTime, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * InventoryItem) |
| void | **[[OnAmmoInitialize]]**() |
| void | **[[OnAnimNotifyStepEvent]]**() |
| void | **[[OnApplyCondition]]**(AActor * Actor, EConditionType Condition) |
| void | **[[OnCharacterLanded]]**(const [FLandedResult](/docs/SDK/Source/Classes/structFLandedResult.md) & LandedResult) |
| void | **[[OnClash]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * InitiatorCharacter, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * TargetCharacter, [FClashEventState](/docs/SDK/Source/Classes/structFClashEventState.md) ClashEventState) |
| void | **[[OnClientPreTravel]]**(const FString & PendingURL, ETravelType TravelType, bool bIsSeamlessTravel) |
| void | **[[OnCombatStateBegin]]**(AActor * Actor, FName State, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * InCombatState) |
| void | **[[OnCombatStateChanged]]**(AActor * Actor, FName PreviousState, FName NewState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * InCombatState) |
| void | **[[OnCombatStateEnd]]**(AActor * Actor, FName State, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * InCombatState) |
| void | **[[OnCombatStateEvent]]**(AActor * Actor, FName EventName, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo) |
| void | **[[OnConstruct]]**(AActor * Actor) |
| void | **[[OnCrowdControlNoDamage]]**(AActor * OwningActor, FName CombatState, [FCrowdControlParams](/docs/SDK/Source/Classes/structFCrowdControlParams.md) CrowdControlParams) |
| void | **[[OnDamageCaused]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & DamageEvent) |
| void | **[[OnDamageTaken]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & DamageEvent) |
| void | **[[OnDismountSiegeEngine]]**([ASiegeEngine](/docs/SDK/Source/Classes/classASiegeEngine.md) * SiegeEngine, bool Forced) |
| void | **[[OnEpicEndGame]]**(const [FEpicEndGameState](/docs/SDK/Source/Classes/structFEpicEndGameState.md) & EpicEndGameState) |
| void | **[[OnExperienceLevelChanged]]**(AActor * Actor, int32 NewLevel) |
| void | **[[OnHealOverTimeAdded]]**(EHealingSource HealingSource, const [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * InstigatingPlayerState) |
| void | **[[OnHealOverTimeEnd]]**() |
| void | **[[OnHealOverTimeStart]]**(EHealingSource HealingSource, const [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * InstigatingPlayerState) |
| void | **[[OnHorseBreakingEvent]]**(bool bIsBreaking, bool bIsEmergencyBreaking, float CurrentSpeed, FName PreviousState) |
| void | **[[OnHorseFxEvent]]**(FName EventName, float EventScale, const TArray< FName > & EventTags) |
| void | **[[OnHorseToCharacterImpact]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * TargetCharacter, EHorseImpactLocation ImpactLocation, EHorseToCharacterImpactType ImpactType, FName ImpactCombatState, float ImpactSpeed) |
| void | **[[OnHorseToHorseImpact]]**([AHorse](/docs/SDK/Source/Classes/classAHorse.md) * TargetHorse, EHorseImpactLocation ImpactLocation, EHorseToHorseImpactType ImpactType, FName ImpactCombatState, float ImpactSpeed) |
| void | **[[OnHorseToWorldImpact]]**(FHitResult Hit, EHorseImpactLocation ImpactLocation, EHorseToWorldImpactType ImpactType, FName ImpactCombatState, float ImpactSpeed) |
| void | **[[OnInventoryActionFailed]]**(EFailedInventoryAction Action) |
| void | **[[OnInventoryItemDamageStateChanged]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item, EInventoryItemDamagedState DamagedState) |
| void | **[[OnInventoryItemDamaged]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item, [FInventoryItemDamagedParams](/docs/SDK/Source/Classes/structFInventoryItemDamagedParams.md) Params) |
| void | **[[OnInventoryProjectileHitPassiveShield]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Shield, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Projectile) |
| void | **[[OnInventoryProjectilePenetratedPassiveShield]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Shield, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Projectile, FVector HitLocation) |
| void | **[[OnInvocationActorCreated]]**(AActor * Actor) |
| void | **[[OnKilled]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & DamageEvent) |
| void | **[[OnMountSiegeEngine]]**([ASiegeEngine](/docs/SDK/Source/Classes/classASiegeEngine.md) * SiegeEngine) |
| void | **[[OnParrySuccess]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * ThisCharacter, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * OtherCharacter, [FParryEventState](/docs/SDK/Source/Classes/structFParryEventState.md) ParryEventState) |
| void | **[[OnPlayerKilled]]**([FDeathEvent](/docs/SDK/Source/Classes/structFDeathEvent.md) DeathEvent) |
| void | **[[OnPlayerMeshChanged]]**(USkeletalMeshComponent * OldMesh, USkeletalMeshComponent * NewMesh) |
| void | **[[OnPossessed]]**(AController * Controller) |
| void | **[[OnRagdollHit]]**(AActor * HitTaker, AActor * HitCauser, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Weapon, const FHitResult & HitResult, const FVector & HitDirection, float Damage, [UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * DamageSource, AActor * Projectile, FName AttackName) |
| void | **[[OnRemoveCondition]]**(AActor * Actor, EConditionType Condition, AActor * ConditionRemover) |
| void | **[[OnSetFirstPersonDeathCamera]]**() |
| void | **[[OnSetOffFire]]**() |
| void | **[[OnSetOnFire]]**() |
| void | **[[OnSetRagdollPhysics]]**() |
| void | **[[OnSetThirdPersonDeathCamera]]**() |
| void | **[[OnStaminaCostFailed]]**(FName Event) |
| void | **[[OnStartedFalling]]**() |
| void | **[[OnStatChanged]]**(AActor * Actor, EStat Type, const [FStatEntry](/docs/SDK/Source/Classes/structFStatEntry.md) & Stat, float DeltaValue) |
| void | **[[OnSuicide]]**(AActor * Suicider, const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & DamageTakenEvent) |
| void | **[[OnTargetMethodEvent]]**(AActor * Initiator, FName TargetMethodName, ETargetMethodEvent::Type Event, const [AAbilityInvocation](/docs/SDK/Source/Classes/classAAbilityInvocation.md) * Invocation, FVector Location, const TArray< AActor * > & HitTargets) |
| void | **[[OnWasParried]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * ThisCharacter, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * OtherCharacter, [FParryEventState](/docs/SDK/Source/Classes/structFParryEventState.md) ParryEventState) |
| void | **[[OnWorldHit]]**(AActor * Actor, FVector Location, UPhysicalMaterial * PhysMaterial) |
| void | **[[ProjectileStarted]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item) |
| void | **[[ProjectileStopped]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item) |
| | **[[UFxEventListener]]**() |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200