---
title: ATBLPlayerState
type: class
aliases: ATBLPlayerState
share: false

---

# ATBLPlayerState





Inherits from APlayerState, [ITBLPlayerStateInterface](/docs/SDK/Source/Classes/classITBLPlayerStateInterface.md)

Inherited by [AArenaPlayerState](/docs/SDK/Source/Classes/classAArenaPlayerState.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ATBLPlayerState]]**() |
| void | **[[AddDeadCharacter]]**(uint8 ID, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * InCharacter, bool bSpawnedHead) |
| void | **[[BroadcastPauseRagdolls]]**(bool bPaused) |
| void | **[[BroadcastStatsLevelUp]]**(TArray< [FLevelUpResult](/docs/SDK/Source/Classes/structFLevelUpResult.md) > NewLevelUpResults) |
| bool | **[[CanBeAutoBalanced]]**() |
| void | **[[ClientBlockInput]]**(bool BlockInput) |
| void | **[[ClientForceReplicate]]**() |
| void | **[[ClientScoreCurveEvent]]**(FName RowName, int32 ScoreCurveAmount, int32 ScoreAmount, [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * Killed, int16 NoveltyScoreRowIndex) |
| void | **[[ClientScoreEvent]]**(FName RowName, int32 ScoreAmount, [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * Killed, int32 Bonuses, int16 NoveltyScoreRowIndex) |
| void | **[[ClientScoreOverrideEvent]]**(FName RowName, int32 ScoreAmount, [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * Killed, int16 NoveltyScoreRowIndex) |
| void | **[[GetAllPresetsAsArray]]**(TArray< [FCustomizationPreset](/docs/SDK/Source/Classes/structFCustomizationPreset.md) > & OutPresets) |
| TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > | **[[GetCharacterClass]]**(bool & IsDead, bool & IsSpectating) |
| EHardwarePlatform | **[[GetClientHardwarePlatform]]**() |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[GetDeadCharacter]]**(uint8 ID) |
| TArray< [FDeathRecapEntry](/docs/SDK/Source/Classes/structFDeathRecapEntry.md) > | **[[GetDeathRecapEntries]]**() |
| void | **[[GetDeathRecapEntryForKiller]]**([FDeathRecapEntry](/docs/SDK/Source/Classes/structFDeathRecapEntry.md) & Entry) |
| void | **[[GetDeathRecapEntryForTakeDowner]]**([FDeathRecapEntry](/docs/SDK/Source/Classes/structFDeathRecapEntry.md) & Entry) |
| FLinearColor | **[[GetDisplayColor]]**() |
| bool | **[[GetIsFriend]]**() const |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| int32 | **[[GetNumInParty]]**() |
| FString | **[[GetPartyId]]**() const |
| TEnumAsByte< EAudioPersonalityType::Type > | **[[GetPersonalityType]]**() const |
| bool | **[[GetPlayerVIPStatus]]**() |
| bool | **[[IsInParty]]**() |
| void | **[[OnRep_AttachToProjectile]]**() |
| void | **[[OnRep_CharacterClass]]**() |
| void | **[[OnRep_NextSpawnTeam]]**() |
| void | **[[OnRep_OnlineStats]]**() |
| void | **[[OnRep_PlatformOSSUniqueId]]**() |
| void | **[[OnRep_PlayFabOSSUniqueId]]**() |
| void | **[[OnRep_Team]]**() |
| void | **[[ResetPartyId]]**() |
| TArray< [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * > | **[[ReturnListOfFriends]]**(TArray< [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * > PlayerStates) |
| void | **[[ServerUpdateFriendStatus]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * MyFriend, bool IsFriend) |
| void | **[[SetIsFriend]]**(bool IsFriend) |
| void | **[[SetNumInParty]]**(int32 inNumInParty) |
| void | **[[SetPartyId]]**(const FString & InPartyId) |
| void | **[[SetPlayerVIPStatus]]**(bool IsVIP) |
| TArray< [FScoreEventStruct](/docs/SDK/Source/Classes/structFScoreEventStruct.md) > | **[[StatsGetPlayerScoreEvents]]**() |
| void | **[[UpdateDeadCharacters]]**() |
| void | **[[UpdatePlayerAutoBalanceEligibility]]**(bool NewCanBeAutoBalanced) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[LocalPlayerPartyCreated]]**(const bool Result, const FString & NewPartyId) |
| void | **[[LocalPlayerPartyDisbanded]]**() |
| void | **[[LocalPlayerPartyInviteAccepted]]**(const FString & NewPartyId) |
| void | **[[LocalPlayerPartyLeft]]**(const bool Result) |
| void | **[[OnPawnDamaged]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & Event) |
| void | **[[OnRep_ClientPlatform]]**() |
| void | **[[OnRep_Deaths]]**() |
| void | **[[OnRep_GlobalRank]]**() |
| void | **[[OnRep_Kills]]**() |
| void | **[[OnRep_NextSpawnPawnSubclass]]**() |
| void | **[[OnRep_OnlineAccount]]**() |
| void | **[[OnRep_PersonalityType]]**() |
| void | **[[OnRep_PlayerScore]]**() |
| void | **[[OnRep_Presets]]**() |
| void | **[[OnRep_Takedowns]]**() |
| void | **[[OnRep_bMustSetLoadout]]**() |
| void | **[[ServerUploadPing]]**(uint8 NewPing) |
| void | **[[SyncScoreEvents]]**(const TArray< [FScoreEventByName](/docs/SDK/Source/Classes/structFScoreEventByName.md) > & ScoreEvents) |
| void | **[[UploadPing]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[AttachToProjectile]]**  |
| [FCustomizationConstraintsQuery](/docs/SDK/Source/Classes/structFCustomizationConstraintsQuery.md) | **[[BotCustomizationQuery]]**  |
| TEnumAsByte< EAudioClassType::Type > | **[[BotSelectedAssetsType]]**  |
| TArray< USkeletalMesh * > | **[[CachedGoreHeadMeshes]]**  |
| USkeletalMesh * | **[[CachedMesh]]**  |
| TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > | **[[CachedMeshClass]]**  |
| EFaction | **[[CachedMeshFaction]]**  |
| TMap< FName, float > | **[[CachedMeshMorphTargets]]**  |
| TArray< [FLevelUpResult](/docs/SDK/Source/Classes/structFLevelUpResult.md) > | **[[CurrentMatchLevelUpResults]]**  |
| uint8 | **[[DeadCharacterId]]**  |
| TMap< uint8, [FDeadCharacter](/docs/SDK/Source/Classes/structFDeadCharacter.md) > | **[[DeadCharacters]]**  |
| [FDeathRecap](/docs/SDK/Source/Classes/structFDeathRecap.md) | **[[DeathRecap]]**  |
| float | **[[DeathTime]]**  |
| TArray< TWeakObjectPtr< [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) > > | **[[DownCausingPlayers]]**  |
| FString | **[[GameSparksUserId]]**  |
| bool | **[[HasBeenAutoBalanced]]**  |
| FDeathsChangedSignature | **[[OnDeathsChanged]]**  |
| FKillsChangedSignature | **[[OnKillsChanged]]**  |
| FNextSpawnTeamChangedSignature | **[[OnNextSpawnTeamChanged]]**  |
| FPlatformChangedSignature | **[[OnPlatformChanged]]**  |
| FScoreEventSignature | **[[OnScoreEvent]]**  |
| FTeamChangedSignature | **[[OnTeamChanged]]**  |
| [FTBLOnlineAccount](/docs/SDK/Source/Classes/structFTBLOnlineAccount.md) | **[[OnlineAccount]]**  |
| FOnlineInventoryRefreshed | **[[OnlineInventoryRefreshed]]**  |
| [FTBLOnlineStats](/docs/SDK/Source/Classes/structFTBLOnlineStats.md) | **[[OnlineStats]]**  |
| FOnlineStatsLevelUp | **[[OnlineStatsLevelUp]]**  |
| FOnlineStatsLogin | **[[OnlineStatsLogin]]**  |
| FOnlineStatsStatValueChanged | **[[OnlineStatsOriginalValueChanged]]**  |
| FOnlineStatsStatValueChanged | **[[OnlineStatsStatValueChanged]]**  |
| FOnlineStatsUpdatedSignature | **[[OnlineStatsUpdated]]**  |
| FOnlineStoreOnCurrencyChanged | **[[OnlineStoreOnCurrencyChanged]]**  |
| FUniqueNetIdRepl | **[[PlatformOSSUniqueId]]**  |
| FUniqueNetIdRepl | **[[PlayFabOSSUniqueId]]**  |
| TArray< AActor * > | **[[RespawnConstructableActors]]**  |
| [FRespawnSpecialItem](/docs/SDK/Source/Classes/structFRespawnSpecialItem.md) | **[[RespawnSpecialItem]]**  |
| TArray< [FStatEntry](/docs/SDK/Source/Classes/structFStatEntry.md) > | **[[RespawnStats]]**  |
| FScoreChangedSignature | **[[ScoreChanged]]**  |
| [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * | **[[TeamBeforeBecameInactive]]**  |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[WaitForAttachToProjectile]]**  |
| bool | **[[bCustomizationUploaded]]**  |
| bool | **[[bReplicateOnlineAccount]]**  |
| bool | **[[bWantsOnlineLoad]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| int32 | **[[ActualStartTime]]**  |
| FLinearColor | **[[AgathaDisplayColor]]**  |
| int32 | **[[Assists]]**  |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[Character]]**  |
| TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > | **[[CharacterClass]]**  |
| EHardwarePlatform | **[[ClientPlatform]]**  |
| FText | **[[CustomizationNickName]]**  |
| TArray< [FTimeStampedDamageTakenEvent](/docs/SDK/Source/Classes/structFTimeStampedDamageTakenEvent.md) > | **[[DamageTakenEvents]]**  |
| int32 | **[[Deaths]]**  |
| TEnumAsByte< EAudioPersonalityType::Type > | **[[EquippedPersonalityType]]**  |
| EFaction | **[[Faction]]**  |
| TArray< [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * > | **[[FriendsList]]**  |
| int32 | **[[GlobalRank]]**  |
| int32 | **[[InactiveTime]]**  |
| TArray< [FInstigatedVote](/docs/SDK/Source/Classes/structFInstigatedVote.md) > | **[[InstigatedVotes]]**  |
| int32 | **[[Kills]]**  |
| TWeakObjectPtr< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > | **[[LastDeathRecapCharacter]]**  |
| float | **[[LastVotedOnTime]]**  |
| FText | **[[LocalizablePlayerName]]**  |
| FLinearColor | **[[MasonDisplayColor]]**  |
| [FLoadout](/docs/SDK/Source/Classes/structFLoadout.md) | **[[NextSpawnLoadout]]**  |
| TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > | **[[NextSpawnPawnSubclass]]**  |
| [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * | **[[NextSpawnTeam]]**  |
| int32 | **[[NumInParty]]**  |
| FOnlineStatsGlobalRankChanged | **[[OnGlobalRankChanged]]**  |
| FTakedownsChangedSignature | **[[OnTakedownsChanged]]**  |
| float | **[[OutOfCombatTimeRemaining]]**  |
| FString | **[[PartyId]]**  |
| int32 | **[[PlayerScore]]**  |
| TArray< [FScoreEventByName](/docs/SDK/Source/Classes/structFScoreEventByName.md) > | **[[PlayerScoreEventsByText]]**  |
| [FReplCustomizationPresetMapping](/docs/SDK/Source/Classes/structFReplCustomizationPresetMapping.md) | **[[Presets]]**  |
| int32 | **[[ProjectilesFired]]**  |
| float | **[[ShowLoadoutDelayTime]]**  |
| FLinearColor | **[[SpectatorDisplayColor]]**  |
| int32 | **[[Takedowns]]**  |
| [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * | **[[Team]]**  |
| FLinearColor | **[[TenosiaDisplayColor]]**  |
| float | **[[TimeSinceLastOutOfCombat]]**  |
| float | **[[TotalIdleTime]]**  |
| float | **[[TotalTeamDamage]]**  |
| TMap< FPrimaryAssetId, EFaction > | **[[WhitelistAssets]]**  |
| bool | **[[bCanBeAutoBalanced]]**  |
| bool | **[[bIsFriend]]**  |
| bool | **[[bIsNPC]]**  |
| bool | **[[bIsNextSpawnLoadoutOverridden]]**  |
| bool | **[[bIsPlayerCustomizedBot]]**  |
| uint8 | **[[bIsVIP]]**  |
| bool | **[[bMustSetLoadout]]**  |
| bool | **[[bQuitter]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200