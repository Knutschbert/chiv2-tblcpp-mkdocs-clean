---
title: UAbilityConfig
type: class
aliases: UAbilityConfig
share: false

---

# UAbilityConfig





Inherits from [UAssemblyBlueprint](/docs/SDK/Source/Classes/classUAssemblyBlueprint.md), UBlueprint

## Public Functions

|                | Name           |
| -------------- | -------------- |
| [UAbilitySpec](/docs/SDK/Source/Classes/classUAbilitySpec.md) * | **[[GetAbilitySpec]]**(FName AbilityName) |
| FName | **[[GetAnimationMontage]]**(FName AbilityName) |
| FName | **[[GetAnimationMontageSection]]**(FName AbilityName) |
| FVector | **[[GetHorseMomentumBasedScale]]**(AActor * InitiatorActor, AActor * TargetActor, FName AbilityName, TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > InventoryItemClass) |
| | **[[UAbilityConfig]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< FString > | **[[AccessGroups]]**  |
| float | **[[ActiveRiposteBlockedStaminaModifier]]**  |
| float | **[[ActiveRiposteWindowTime]]**  |
| [FAimPenaltySettings](/docs/SDK/Source/Classes/structFAimPenaltySettings.md) | **[[AimPenalty]]**  |
| TSoftClassPtr< [AHorse](/docs/SDK/Source/Classes/classAHorse.md) > | **[[ArmoredHorseClass]]**  |
| float | **[[BlockingArrowDamageModifier]]**  |
| [FBlockingCategoryModifier](/docs/SDK/Source/Classes/structFBlockingCategoryModifier.md) | **[[BlockingCategoryStaminaModifier]]**  |
| float | **[[BowAgainstArcherDamageModifier]]**  |
| float | **[[CanSprintInAirTime]]**  |
| float | **[[CancelCooldown]]**  |
| int32 | **[[ChanceToLogAbilityEvents]]**  |
| TArray< [FOnlineClassXp](/docs/SDK/Source/Classes/structFOnlineClassXp.md) > | **[[ClassXps]]**  |
| TArray< TSubclassOf< [UCombatStateSet](/docs/SDK/Source/Classes/classUCombatStateSet.md) > > | **[[CombatStateSets]]**  |
| float | **[[ComboCancelInputWindow]]**  |
| float | **[[ComboCancelTriggerEndWindow]]**  |
| float | **[[ComboFromBlockedTime]]**  |
| float | **[[ComboFromMissedAttackTime]]**  |
| TArray< [URewardTable](/docs/SDK/Source/Classes/classURewardTable.md) * > | **[[CookedTreasureTables]]**  |
| float | **[[CounterBlockedStaminaModifier]]**  |
| float | **[[CounterFeintEndWindow]]**  |
| float | **[[CounterSuccessExtendWindowTime]]**  |
| float | **[[CounterWindowGapTime]]**  |
| float | **[[DamageItemDelayTimeSeconds]]**  |
| [FDeathRecapLimits](/docs/SDK/Source/Classes/structFDeathRecapLimits.md)[4] | **[[DeathRecapLimits]]**  |
| TSubclassOf< [UFxInstance](/docs/SDK/Source/Classes/classUFxInstance.md) > | **[[DefaultAbilityClass]]**  |
| [FDownedSprintStamina](/docs/SDK/Source/Classes/structFDownedSprintStamina.md) | **[[DownedSprintStamina]]**  |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[DownedWeapon]]**  |
| float | **[[FakeClientProjectileInterpolateExp]]**  |
| float | **[[FakeClientProjectileInterpolateTime]]**  |
| float | **[[FallingTime]]**  |
| float | **[[FeintComboAnimPercentThreshold]]**  |
| float | **[[FeintEndWindow]]**  |
| float | **[[FeintMaxTransitionTargetPercent]]**  |
| [FFeintMinTime](/docs/SDK/Source/Classes/structFFeintMinTime.md) | **[[FeintMinTime]]**  |
| [FFeintTime](/docs/SDK/Source/Classes/structFFeintTime.md) | **[[FeintTime]]**  |
| [FFocusSettings](/docs/SDK/Source/Classes/structFFocusSettings.md) | **[[FocusSettings]]**  |
| float | **[[GamepadCancelWindow]]**  |
| float | **[[GlobalStaminaModifier]]**  |
| int32 | **[[GlobalXp]]**  |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[GoreHeadItem]]**  |
| TSoftClassPtr< [AHorse](/docs/SDK/Source/Classes/classAHorse.md) > | **[[HorseClass]]**  |
| float | **[[HorseScoreBonusDamageThreshold]]**  |
| [FFocusSettings](/docs/SDK/Source/Classes/structFFocusSettings.md) | **[[HorseSpecialFocusSettings]]**  |
| [FHorseStaminaCosts](/docs/SDK/Source/Classes/structFHorseStaminaCosts.md) | **[[HorseStaminaCosts]]**  |
| float | **[[IsLookingDownAngle]]**  |
| float | **[[JabFromDashAttackTime]]**  |
| float | **[[KickLowAngle]]**  |
| TSoftClassPtr< [UHudMarkerDisplayComponent](/docs/SDK/Source/Classes/classUHudMarkerDisplayComponent.md) > | **[[LTSHudMarkerComponentClass]]**  |
| [FFocusSettings](/docs/SDK/Source/Classes/structFFocusSettings.md) | **[[LanceChargeFocusSettings]]**  |
| [FLocationBasedDamageModifiers](/docs/SDK/Source/Classes/structFLocationBasedDamageModifiers.md) | **[[LocationBasedDamageModifiers]]**  |
| float | **[[MaxClashCameraAngle]]**  |
| float | **[[MaxCounterWindowTime]]**  |
| float | **[[MaxRecentlyAwardedPlaytime]]**  |
| float | **[[MinCounterWindowTime]]**  |
| float | **[[ParryBoxAngle]]**  |
| float | **[[ParryBreakDamageModifier]]**  |
| bool | **[[ParryBreakNonFatal]]**  |
| float | **[[ParryBreakStamina]]**  |
| float | **[[ParryBreakStaminaDelay]]**  |
| float | **[[ParryComboTiming]]**  |
| float | **[[ParryDisableStaminaDrainTime]]**  |
| float | **[[ParryForgivenessWindowTime]]**  |
| float | **[[ParryReduceStaminaRate]]**  |
| float | **[[ParryReduceStaminaTime]]**  |
| float | **[[PercentChanceToPlayRagdollInsteadOfAnimation]]**  |
| float | **[[PercentChanceToPlayRootMotionDeathAnimation]]**  |
| UCurveFloat * | **[[PlaytimeAwardCurve]]**  |
| [URewardTable](/docs/SDK/Source/Classes/classURewardTable.md) * | **[[PlaytimeDropTable]]**  |
| float | **[[PlaytimeForItem]]**  |
| float | **[[ProjectileCounterWindowTime]]**  |
| [FProjectileHUDConfig](/docs/SDK/Source/Classes/structFProjectileHUDConfig.md) | **[[ProjectileHUD]]**  |
| [FLocationBasedDamageModifiers](/docs/SDK/Source/Classes/structFLocationBasedDamageModifiers.md) | **[[RangedLocationBasedDamageModifiers]]**  |
| float | **[[RemainInSprintBelowMinSpeedTime]]**  |
| float | **[[RevivedStamina]]**  |
| TArray< FName > | **[[RewardTokens]]**  |
| float | **[[RiposteParryWindow]]**  |
| float | **[[SiegeAgainstCatapultDamageModifier]]**  |
| float | **[[SpecialAbilityHealingScoreModifier]]**  |
| [FSpecialItemCharge](/docs/SDK/Source/Classes/structFSpecialItemCharge.md) | **[[SpecialItemCharge]]**  |
| float | **[[SprintAttackSpeed]]**  |
| [FStaminaBonus](/docs/SDK/Source/Classes/structFStaminaBonus.md) | **[[StaminaBonus]]**  |
| [FStaminaCosts](/docs/SDK/Source/Classes/structFStaminaCosts.md) | **[[StaminaCosts]]**  |
| float | **[[ThrownStaminaModifier]]**  |
| float | **[[ThwackTracerLengthPercent]]**  |
| float | **[[TurnLimitEndTime]]**  |
| bool | **[[bDebugSounds]]**  |
| bool | **[[bMuteServerSounds]]**  |
| bool | **[[bOnlyClashOnHorseVsHorse]]**  |
| bool | **[[bRiposteUsesParriedComboStateOnlyForSlash]]**  |
| bool | **[[bScaleRecoveryAnimiation]]**  |
| bool | **[[bShouldCooldownRefreshStatesResetCooldowns]]**  |
| bool | **[[bUseClashCameraAngleCheck]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< FName > | **[[AttackNames]]**  |
| TMap< FName, uint8 > | **[[AttackNamesToIndex]]**  |
| TMap< FName, uint8 > | **[[CharacterMovementStateToIndex]]**  |
| TArray< FName > | **[[CharacterMovementStates]]**  |
| TArray< FName > | **[[CombatStateNames]]**  |
| TMap< FName, uint8 > | **[[CombatStateNamesToIndex]]**  |
| TMap< FName, uint8 > | **[[InputActionNameToIndex]]**  |
| TArray< FName > | **[[InputActionNames]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200