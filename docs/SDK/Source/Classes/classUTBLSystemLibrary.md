---
title: UTBLSystemLibrary
type: class
aliases: UTBLSystemLibrary
share: false

---

# UTBLSystemLibrary





Inherits from UBlueprintFunctionLibrary

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AddClosedCaptionLine]]**(FText OriginString, FText ChatString, AActor * OriginatingActor, EClosedCaptionType Type, UObject * WorldContextObject, bool IgnoreDistance) |
| bool | **[[AddTagsToActor]]**(AActor * Actor, TArray< FName > Tags, UObject * WorldContextObject) |
| bool | **[[AreHardwarePlatformsFromTheSameFirstParty]]**(EHardwarePlatform A, EHardwarePlatform B) |
| void | **[[AtlasCharacterTextures]]**(ACharacter * Character) |
| USceneComponent * | **[[AttachComponentFromSCS]]**(UClass * Class, AActor * TargetActor, USceneComponent * TargetComponent, FName ComponentName) |
| void | **[[AwardOverrideScoreToPlayer]]**(FName RowName, int32 Score, [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * Player, [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * OtherPlayer) |
| void | **[[AwardScoreToPlayers]]**(UObject * WorldContextObject, TArray< [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * > PlayerStates, FName RowName, EOnlineStat Stat) |
| void | **[[BeginProfilerStat]]**(const [FProfilerStat](/docs/SDK/Source/Classes/structFProfilerStat.md) & ProfilerStat) |
| bool | **[[BlueprintOnlineUserEquals]]**(const [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) & A, const [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) & B) |
| void | **[[BreakCanvasIcon]]**(FCanvasIcon Icon, UTexture *& Texture, float & U, float & V, float & UL, float & VL) |
| bool | **[[CanCharacterSubclassUsePrimaryWeapon]]**(TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > CharacterSubclass, TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > PrimaryWeapon) |
| void | **[[CancelAllLatentActionsForObject]]**(UObject * Object) |
| void | **[[ClearCharacterRuntimeAssetCache]]**() |
| AActor * | **[[CreateSoundActor]]**(AActor * ReferenceActor, FVector OffsetLocation) |
| [UStatsComponent](/docs/SDK/Source/Classes/classUStatsComponent.md) * | **[[CreateStatsComponent]]**(AActor * Actor) |
| void | **[[DestroyActorComponent]]**(UActorComponent * Component) |
| void | **[[DisableComponentsOnBotClient]]**(AActor * Actor) |
| void | **[[DisableComponentsOnServer]]**(AActor * Actor, int32 DisableFlags) |
| void | **[[DoKeyAxis]]**(AActor * Actor, FName ActionName, float AxisValue) |
| void | **[[DoKeyEvent]]**(AActor * Actor, FName ActionName, TEnumAsByte< EInputEvent > KeyEvent) |
| bool | **[[DoesActorHaveInventoryItem]]**(AActor * Actor, TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > InventoryItem, bool bCanBeChildOf) |
| void | **[[DumpPlayers]]**(UWorld * World) |
| void | **[[EndProfilerStat]]**(const [FProfilerStat](/docs/SDK/Source/Classes/structFProfilerStat.md) & ProfilerStat) |
| UClass * | **[[FindBlueprintClass]]**(const FString & BlueprintName, UClass * ParentClass) |
| void | **[[ForcePlayerDropCarryable]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character, TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > InventoryType) |
| void | **[[ForcePlayersDropCarryable]]**(UObject * WorldContextObject, EFaction Faction, TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > InventoryType) |
| void | **[[ForceUpdateChildTransforms]]**(USceneComponent * Component) |
| TArray< [FGameModeMessage](/docs/SDK/Source/Classes/structFGameModeMessage.md) > | **[[FormatGameModeMessages]]**(TArray< [FGameModeMessageTable](/docs/SDK/Source/Classes/structFGameModeMessageTable.md) > Messages) |
| void | **[[FrameDelay]]**(UObject * WorldContextObject, int32 NumFramesToDelay, FLatentActionInfo LatentInfo) |
| FLinearColor | **[[GammaCorrectLinearColor]]**(FLinearColor LinCol, float Gamma) |
| FString | **[[GenerateHashName]]**(const FString & StringToHash, ENameType NameType) |
| FString | **[[GenerateRandomName]]**(ENameType NameType) |
| [UAbilitiesComponent](/docs/SDK/Source/Classes/classUAbilitiesComponent.md) * | **[[GetAbilitiesComponent]]**(AActor * Actor) |
| [UAbilityConfig](/docs/SDK/Source/Classes/classUAbilityConfig.md) * | **[[GetAbilityConfig]]**(UObject * WorldContextObject) |
| bool | **[[GetAbilityConfigLoaded]]**(UObject * WorldContextObject) |
| FText | **[[GetActionBindingTextForInventorySlot]]**(EInventoryItemSlot InventoryItemSlot, UObject * WorldContextObject, FInputActionKeyMapping & ActionMapping) |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[GetActorAttackingWeapon]]**(const AActor * Actor) |
| UActorComponent * | **[[GetActorComponent]]**(AActor * Actor, TSubclassOf< UActorComponent > Class) |
| UActorComponent * | **[[GetActorComponentWithTag]]**(AActor * Actor, FName Tag) |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[GetActorEquippedWeapon]]**(const AActor * Actor) |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[GetActorEquippedWeaponByState]]**(const AActor * Actor, EEquippedState EquippedState) |
| EFaction | **[[GetActorFaction]]**(const AActor * Actor) |
| void | **[[GetActorMaterials]]**(AActor * Actor, TArray< UPrimitiveComponent * > & OutComponents, TArray< UMaterialInstanceDynamic * > & OutMaterials) |
| [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * | **[[GetActorTeam]]**(AActor * Actor) |
| TArray< AActor * > | **[[GetActorsWithTag]]**(const FName & Tag, UObject * WorldContextObject) |
| void | **[[GetActorsWithTagClassSpecifier]]**(FName Tag, TSubclassOf< AActor > ActorClass, const UObject * WorldContextObject, TArray< AActor * > & OutActors) |
| TArray< AActor * > | **[[GetAllActorsWithComponents]]**(const TArray< TSubclassOf< UActorComponent >> & ComponentClasses, UObject * WorldContextObject) |
| TArray< AActor * > | **[[GetAllActorsWithComponentsWithExclusions]]**(const TArray< TSubclassOf< UActorComponent >> & ComponentClasses, const TArray< TSubclassOf< UActorComponent >> & ExcludeComponentClasses, const TArray< TSubclassOf< AActor >> & OptionalActorClasses, UObject * WorldContextObject) |
| void | **[[GetAllActorsWithTag]]**(const UObject * WorldContextObject, FName Tag, TArray< AActor * > & OutActors) |
| TArray< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * > | **[[GetAllCharactersFromFaction]]**(UObject * WorldContextObject, EFaction Faction) |
| TArray< UActorComponent * > | **[[GetAllComponentsFromClass]]**(TSubclassOf< AActor > ActorClass) |
| TArray< FString > | **[[GetAllFrontendMovieURLs]]**() |
| void | **[[GetAllMapNames_EditorOnly]]**(TArray< FString > & MapNames) |
| TArray< FString > | **[[GetAllNames]]**(ENameType NameType) |
| void | **[[GetAllTeamsPlayersWithExclusion]]**(UObject * WorldContextObject, TArray< EFaction > ExcludeFactions, TArray< [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * > & IncludedTeams, TArray< AController * > & IncludedPlayers) |
| [AAlwaysOnMusicManager](/docs/SDK/Source/Classes/classAAlwaysOnMusicManager.md) * | **[[GetAlwaysOnMusicManager]]**(UObject * WorldContextObject) |
| TArray< AActor * > | **[[GetAttachedActors]]**(AActor * Actor) |
| EFaction | **[[GetAttackingFaction]]**(const UObject * WorldContextObject) |
| EBuildFinality | **[[GetBuildFinality]]**() |
| FString | **[[GetBuildNumber]]**() |
| TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > | **[[GetCharacterClassFromSubclass]]**(TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > Subclass) |
| TEnumAsByte< EAudioClassType::Type > | **[[GetCharacterClassType]]**(AActor * Actor) |
| TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > | **[[GetCharacterSubclassForPrimaryWeapon]]**(TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > CharacterClass, TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > PrimaryWeapon) |
| TArray< TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > > | **[[GetCharacterSubclasses]]**(TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > ParentClass) |
| TArray< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * > | **[[GetCharactersFromFactions]]**(UObject * WorldContextObject, TArray< EFaction > Factions, bool AllowBots, bool AllowNPCs) |
| FString | **[[GetClassPathName]]**(const UClass * InClass) |
| [UConditionsComponent](/docs/SDK/Source/Classes/classUConditionsComponent.md) * | **[[GetConditionsComponent]]**(AActor * Actor) |
| [UContextVOManager](/docs/SDK/Source/Classes/classUContextVOManager.md) * | **[[GetContextVoObject]]**(const UObject * WorldContextObject) |
| TArray< AController * > | **[[GetControllersFromFaction]]**(UObject * WorldContextObject, EFaction Faction) |
| ECrowdControlDirection | **[[GetCrowdControlDirection]]**(FName Direction) |
| FString | **[[GetCurrencyIdCrowns]]**() |
| FString | **[[GetCurrencyIdGold]]**() |
| FString | **[[GetCurrencyIdReal]]**() |
| FString | **[[GetCurrentServerNameString]]**(UObject * WorldContextObject) |
| bool | **[[GetCustomPersonalityEmoteOverride]]**([FPersonalityEmoteTableRow](/docs/SDK/Source/Classes/structFPersonalityEmoteTableRow.md) Emote, TEnumAsByte< EAudioPersonalityType::Type > PersonalityType, [FPersonalityEmoteTableRow](/docs/SDK/Source/Classes/structFPersonalityEmoteTableRow.md) & OutRow) |
| TArray< [FCustomPersonalityEmotesTableRow](/docs/SDK/Source/Classes/structFCustomPersonalityEmotesTableRow.md) > | **[[GetCustomPersonalityEmotes]]**() |
| [UCustomizationComponent](/docs/SDK/Source/Classes/classUCustomizationComponent.md) * | **[[GetCustomizationComponent]]**(AActor * Actor) |
| FText | **[[GetDamageSourceDisplayName]]**(const [UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * DamageSource) |
| UTexture * | **[[GetDamageSourceIconTexture]]**(const [UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * DamageSource) |
| FName | **[[GetDamageSourceName]]**(const [UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * DamageSource) |
| FDateTime | **[[GetDateTime]]**(const [FReplicatedDateTime](/docs/SDK/Source/Classes/structFReplicatedDateTime.md) & ReplDateTime) |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[GetDefaultCharacterFromCharacterClass]]**(TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > CharacterClass) |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[GetDefaultInventoryItemObject]]**(TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > InventoryItemClass) |
| UObject * | **[[GetDefaultObjectFromStringReference]]**(const FSoftObjectPath & StringReference) |
| EFaction | **[[GetDefendingFaction]]**(const UObject * WorldContextObject) |
| FString | **[[GetDemoPlayerName]]**(UObject * WorldContextObject) |
| FString | **[[GetDemoServer]]**(UObject * WorldContextObject) |
| int32 | **[[GetDemoTeam]]**(UObject * WorldContextObject) |
| [UTBLDialogManager](/docs/SDK/Source/Classes/classUTBLDialogManager.md) * | **[[GetDialogManager]]**(UObject * WorldContextObject) |
| void | **[[GetDisplayInfoFromCharacterClass]]**(TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > CharacterClass, [FCharacterDisplayInfo](/docs/SDK/Source/Classes/structFCharacterDisplayInfo.md) & DisplayInfo) |
| FString | **[[GetFriendDisplayName]]**(const [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) & InFriend) |
| FString | **[[GetFriendUserId]]**(const [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) & InFriend) |
| FString | **[[GetFullBuildVersionString]]**() |
| TArray< [FGameModeMessageTable](/docs/SDK/Source/Classes/structFGameModeMessageTable.md) > | **[[GetGameModeMessageRows]]**(UDataTable * GameModeMessageDataTable, TArray< FString > EventTags) |
| FString | **[[GetGameModeNameString]]**(UObject * WorldContextObject) |
| FName | **[[GetHitDirectionName]]**(AActor * HitActor, FVector HitDirection) |
| UTexture2D * | **[[GetIconFromCharacterClass]]**(TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > CharacterClass) |
| FText | **[[GetInventorySlotTextFromEnum]]**(EInventorySlot InventorySlotType) |
| AActor * | **[[GetKilledActor]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & Event) |
| float | **[[GetLastServerReceivePacketTime]]**(UObject * WorldContextObject) |
| ALevelScriptActor * | **[[GetLevelScriptActor]]**(UObject * WorldContextObject) |
| [ULoadoutSelection](/docs/SDK/Source/Classes/classULoadoutSelection.md) * | **[[GetLoadoutSelectionDefaultObj]]**(TSubclassOf< [ULoadoutSelection](/docs/SDK/Source/Classes/classULoadoutSelection.md) > LoadoutSelectionClass) |
| FText | **[[GetLocalizedCharacterClassText]]**(ECharacterClass CharacterClass) |
| bool | **[[GetLocalizedGameModeFromMapString]]**(const FString & MapNameString, FText & LongForm, FText & ShortForm) |
| FText | **[[GetLocalizedGameModeTypeText]]**(TEnumAsByte< EGameModeType::Type > GamemodeType) |
| FText | **[[GetLocalizedItemLevelTypeText]]**(EOnlineStat ItemLevelType) |
| FText | **[[GetLocalizedMapName]]**(const FString & MapNameString, FString & MapNameKey) |
| FText | **[[GetLocalizedTextFromItemUnlock]]**(TEnumAsByte< EOnlineItemUnlockType::Type > ItemUnlockType) |
| FText | **[[GetLocalizedWeaponTagText]]**(EWeaponTag WeaponTag) |
| FString | **[[GetMapNameString]]**(UObject * WorldContextObject) |
| [UTBLMapSummary](/docs/SDK/Source/Classes/classUTBLMapSummary.md) * | **[[GetMapSummary]]**(UObject * WorldContextObject, const FString & MapFileNameWithOptions, bool bCheckGameInstance) |
| float | **[[GetMaxFloat]]**() |
| int32 | **[[GetMaxPlayersForServer]]**(UObject * WorldContextObject) |
| UMovementComponent * | **[[GetMovementComponent]]**(AActor * Actor) |
| [UMovementModifierComponent](/docs/SDK/Source/Classes/classUMovementModifierComponent.md) * | **[[GetMovementModifierComponent]]**(AActor * Actor) |
| bool | **[[GetNDASigned]]**(UObject * WorldContextObject) |
| FText | **[[GetNameFromCharacterClass]]**(TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > CharacterClass) |
| float | **[[GetNegativeMaxFloat]]**() |
| FVector | **[[GetNegativeMaxFloatVector]]**() |
| [FTeamDisplayInfo](/docs/SDK/Source/Classes/structFTeamDisplayInfo.md) | **[[GetNeutralTeamDisplayInfo]]**(UObject * WorldContextObject) |
| int32 | **[[GetNumPlayers]]**(UObject * WorldContextObject, bool IncludeBots, bool IncludeNPCs) |
| FText | **[[GetObjectiveScoreTextFromEnum]]**(TEnumAsByte< EObjectivePointCategory::Type > ObjPointCat) |
| int32 | **[[GetOnlineStatBattlecries]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * PlayerState) |
| int32 | **[[GetOnlineStatCommendations]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * PlayerState) |
| EOnlineStat | **[[GetOnlineStatFromCharacterClass]]**(ECharacterClass CharacterClass) |
| EOnlineStat | **[[GetOnlineStatFromWeaponTag]]**(EWeaponTag WeaponTag) |
| int32 | **[[GetOnlineStatSubClassDeaths]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * PlayerState, ECharacterClass CharacterClass) |
| int32 | **[[GetOnlineStatSubClassKills]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * PlayerState, ECharacterClass CharacterClass) |
| int32 | **[[GetOnlineStatSubClassPlaytime]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * PlayerState, ECharacterClass CharacterClass) |
| int32 | **[[GetOnlineStatSubClassTakedowns]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * PlayerState, ECharacterClass CharacterClass) |
| int32 | **[[GetOnlineStatWeaponDeaths]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * PlayerState, EWeaponTag Weapon) |
| int32 | **[[GetOnlineStatWeaponKills]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * PlayerState, EWeaponTag Weapon) |
| int32 | **[[GetOnlineStatWeaponTakedowns]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * State, EWeaponTag WeaponTag) |
| EFaction | **[[GetOppositeFaction]]**(const UObject * WorldContextObject, EFaction Faction) |
| [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * | **[[GetOppositeTeam]]**(UObject * WorldContextObject, [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * Team) |
| TArray< [FPersonalityEmoteTableRow](/docs/SDK/Source/Classes/structFPersonalityEmoteTableRow.md) > | **[[GetPersonalityEmotes]]**() |
| [FactionNumbers](/docs/SDK/Source/Classes/structFactionNumbers.md) | **[[GetPlayerCountsFromFaction]]**(UObject * WorldContextObject, EFaction Faction) |
| FString | **[[GetPlayerDebugName]]**(APlayerState * PlayerState) |
| [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * | **[[GetPlayerStateFromUniqueNetId]]**(UObject * WorldContextObject, const FUniqueNetIdRepl & UniqueId) |
| TArray< [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * > | **[[GetPlayerStates]]**(UObject * WorldContextObject) |
| TArray< [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * > | **[[GetPlayerStatesFromFaction]]**(UObject * WorldContextObject, EFaction Faction) |
| TArray< AController * > | **[[GetPlayersFromFactions]]**(UObject * WorldContextObject, TArray< EFaction > Factions, bool AllowBots, bool AllowNPCs) |
| AActor * | **[[GetPossessorActor]]**(AActor * Actor) |
| TArray< [FGameModeMessageTable](/docs/SDK/Source/Classes/structFGameModeMessageTable.md) > | **[[GetScoredStageGameModeMessageRows]]**(UDataTable * GameModeMessageDataTable, int32 StageNum, int32 NewScore, int32 LastScore) |
| FVector | **[[GetScreenPositionForActor]]**(APlayerController * PlayerController, AActor * Actor, const FVector & RelativeLocation, bool bUseActorBoundsOrigin) |
| FVector | **[[GetScreenPositionForLocation]]**(APlayerController * PlayerController, const FVector & Location) |
| float | **[[GetServerTimeoutTime]]**(UObject * WorldContextObject) |
| bool | **[[GetShowBigNotification]]**(UObject * WorldContextObject) |
| UFont * | **[[GetSmallFont]]**() |
| UStaticMeshComponent * | **[[GetStaticMeshComponent]]**(AActor * Actor) |
| [UStatsComponent](/docs/SDK/Source/Classes/classUStatsComponent.md) * | **[[GetStatsComponent]]**(AActor * Actor) |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[GetTBLCharacter]]**(APawn * Pawn) |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[GetTBLCharacterFromController]]**(const AController * Controller) |
| [ATBLGameMode](/docs/SDK/Source/Classes/classATBLGameMode.md) * | **[[GetTBLGameMode]]**(UObject * WorldContextObject) |
| [ATBLGameState](/docs/SDK/Source/Classes/classATBLGameState.md) * | **[[GetTBLGameState]]**(UObject * WorldContextObject) |
| [UTBLGameUserSettings](/docs/SDK/Source/Classes/classUTBLGameUserSettings.md) * | **[[GetTBLGameUserSettings]]**() |
| [ATBLLevelScriptActor](/docs/SDK/Source/Classes/classATBLLevelScriptActor.md) * | **[[GetTBLLevelScriptActor]]**(UObject * WorldContextObject, bool & bIsValid) |
| [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * | **[[GetTeamFromFaction]]**(UObject * WorldContextObject, EFaction Faction) |
| TArray< [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * > | **[[GetTeamsFromFactions]]**(UObject * WorldContextObject, TArray< EFaction > Factions) |
| FText | **[[GetTextFromNamespace]]**(const FString & Namespace, const FString & Key) |
| float | **[[GetTimeSeconds]]**(AActor * Actor) |
| UFont * | **[[GetTinyFont]]**() |
| int32 | **[[GetTotalPlayerCount]]**(UObject * WorldContextObject) |
| FString | **[[GetUnlocalizedGameModeFromMapString]]**(const FString & MapNameString) |
| TEnumAsByte< ETBLWorldType::Type > | **[[GetWorldType]]**(UObject * WorldContextObject) |
| bool | **[[HasActorBegunPlay]]**(AActor * Actor) |
| bool | **[[HasRole]]**(AActor * Actor, int32 Role) |
| void | **[[InterpolateFloatOverTime]]**(UObject * WorldContextObject, float StartValue, float EndValue, float Duration, bool bEaseOut, bool bEaseIn, float EasingExp, UCurveFloat * Curve, FInterpolatorFloatUpdated UpdateDelegate, TEnumAsByte< EInterpolateOverTimeAction::Type > InterpolateAction, FLatentActionInfo LatentInfo, bool bCallUpdatesParams) |
| void | **[[InterpolateVectorOverTime]]**(UObject * WorldContextObject, FVector StartValue, FVector EndValue, float Duration, bool bEaseOut, bool bEaseIn, float EasingExp, UCurveFloat * Curve, FInterpolatorVectorUpdated UpdateDelegate, TEnumAsByte< EInterpolateOverTimeAction::Type > InterpolateAction, FLatentActionInfo LatentInfo, bool bCallUpdatesParams) |
| bool | **[[IsAttackingFaction]]**(const UObject * WorldContextObject, EFaction Faction) |
| bool | **[[IsAutomationTesting]]**() |
| bool | **[[IsBot]]**(AActor * Actor) |
| bool | **[[IsControllerMounted]]**(AController * Controller, TSubclassOf< [ASiegeEngine](/docs/SDK/Source/Classes/classASiegeEngine.md) > SiegeEngineClass) |
| bool | **[[IsDamageExemptFromTeamDamage]]**(AActor * DamageCauser, [UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * DamageSource) |
| bool | **[[IsDefendingFaction]]**(const UObject * WorldContextObject, EFaction Faction) |
| bool | **[[IsDemoMode]]**(const UObject * WorldContextObject) |
| bool | **[[IsFirstMainMenuLoad]]**() |
| bool | **[[IsMergedMaterial]]**(ACharacter * Character) |
| bool | **[[IsMergedMesh]]**(ACharacter * Character) |
| bool | **[[IsNonSpecificTeamFaction]]**(EFaction Faction) |
| bool | **[[IsOfficialServer]]**() |
| bool | **[[IsPartOfFaction]]**(EFaction Target, EFaction Other) |
| bool | **[[IsRangedOrThrownAttack]]**(FName AttackName) |
| bool | **[[IsRangedWeapon]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Weapon) |
| bool | **[[IsRunningAutomatedTesting]]**(UObject * WorldContextObject) |
| bool | **[[IsSimulatingInEditor]]**() |
| bool | **[[IsSoundEnabled]]**(UObject * WorldContextObject) |
| bool | **[[IsSpecificTeamFaction]]**(EFaction Faction) |
| bool | **[[IsSteamInitialized]]**() |
| bool | **[[IsThrownImpactSoundDebugEnabled]]**(UObject * WorldContextObject) |
| bool | **[[IsTutorial]]**(UObject * WorldContextObject) |
| bool | **[[IsValidClassID]]**(const TSoftClassPtr< [UTBLScreenWidget](/docs/SDK/Source/Classes/classUTBLScreenWidget.md) > & ClassID) |
| bool | **[[IsValidHorseServer]]**(UObject * WorldContextObject) |
| bool | **[[IsValidUser]]**(const [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) & InUser) |
| bool | **[[IsWindowsOSSInitialized]]**() |
| void | **[[LevelBlueprintEvent]]**(UObject * WorldContextObject, FName EventName) |
| TScriptInterface< [IStageInterface](/docs/SDK/Source/Classes/classIStageInterface.md) > | **[[LevelBlueprintGetFirstStage]]**(UObject * WorldContextObject) |
| UClass * | **[[LoadSoftClassSynchronously]]**(TSoftClassPtr< UObject > SoftClassRef, UObject * WorldContextObject) |
| UObject * | **[[LoadSoftObjectSynchronously]]**(TSoftObjectPtr< UObject > SoftObjectRef, UObject * WorldContextObject) |
| [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) | **[[MakeDamageTakenEvent]]**(float InDamage, [UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * InDamageSource, AActor * InDamageCauser, AActor * InDamageTaker, AActor * InDamageInstigator, bool InbKillingBlow, bool InbSuicide, bool InbEnteredKillVolume, FHitResult InHitResult, [UAbilitySpec](/docs/SDK/Source/Classes/classUAbilitySpec.md) * InAbilitySpec, FVector_NetQuantizeNormal InHitDirection, FName InDamageTakerCombatState, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * InInventoryItem, AActor * InProjectile, FName InAttackName) |
| [FGoreEvent](/docs/SDK/Source/Classes/structFGoreEvent.md) | **[[MakeGoreEvent]]**(FName InBoneName, EHeadGoreAction InHeadGoreAction, ELimbGoreAction InLimbGoreAction, FVector InImpulse, bool bInSpawnedItem, bool bKillingBlow) |
| void | **[[MarkReplicationDirty]]**(const TScriptInterface< [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md) > & ReplicatedSubobject) |
| void | **[[PlayDemo]]**(const FString & DemoName, UObject * WorldContextObject) |
| int32 | **[[PlaySoundAtLocation]]**(UAkAudioEvent * SoundEvent, const FVector & Location, const FRotator & Rotation, UObject * WorldContextObject, bool bPrintEvents) |
| int32 | **[[PlaySoundAtLocationWithParams]]**(UAkAudioEvent * SoundEvent, const FVector & Location, const FRotator & Rotation, const TArray< [FSoundStateEntry](/docs/SDK/Source/Classes/structFSoundStateEntry.md) > & States, const TArray< [FSoundRTPCEntry](/docs/SDK/Source/Classes/structFSoundRTPCEntry.md) > & RtpcValues, UObject * WorldContextObject, bool bPrintEvents) |
| UAkComponent * | **[[PlaySoundOnActor]]**(UAkAudioEvent * SoundEvent, AActor * Actor, FName AttachSocket, bool bPrintEvents) |
| UAkComponent * | **[[PlaySoundOnActorWithParams]]**(UAkAudioEvent * SoundEvent, AActor * Actor, FName AttachSocket, const TArray< [FSoundSwitchEntry](/docs/SDK/Source/Classes/structFSoundSwitchEntry.md) > & Switches, const TArray< [FSoundRTPCEntry](/docs/SDK/Source/Classes/structFSoundRTPCEntry.md) > & RtpcValues, bool bPrintEvents) |
| FString | **[[RemovePiePrefixFromMapName]]**(const FString & MapNameString) |
| void | **[[RemovePlayersInPartiesFromPlayerStateArray]]**(TArray< [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * > & PlayerStates) |
| void | **[[RemovePlayersWhoAreDeadFromPlayerStateArray]]**(TArray< [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * > & PlayerStates) |
| void | **[[RemoveTagFromActor]]**(AActor * Actor, FName Tag, UObject * WorldContextObject) |
| void | **[[RemoveTagFromAllActors]]**(FName Tag, UObject * WorldContextObject) |
| void | **[[RenameComponentToStableName]]**(UActorComponent * Component, const FString & NamePrefix, int32 ComponentId) |
| [FReplicatedDateTime](/docs/SDK/Source/Classes/structFReplicatedDateTime.md) | **[[ReplicatedDateTime]]**(const FDateTime & ReplDateTime) |
| void | **[[SetActorComponentCanAffectNavigation]]**(UActorComponent * Component, bool bCanAffectNavigation) |
| void | **[[SetAlwaysOnMusicManagerState]]**(UObject * WorldContextObject, EAlwaysOnMusicState NewState) |
| void | **[[SetComponentsEnabled]]**(AActor * Actor, int32 ComponentFlags, bool bEnabled) |
| void | **[[SetNDASigned]]**(bool NDASigned, UObject * WorldContextObject) |
| FTimerHandle | **[[SetNonResettingTimer]]**(UObject * WorldContextObject, float Time, bool Looping, FBlueprintNonResettingTimeExpired Event) |
| void | **[[SetShowBigNotification]]**(UObject * WorldContextObject) |
| void | **[[SetupBlueprintVolumeSubclassBrushInConstructionScript]]**(AVolume * Volume) |
| void | **[[SetupCubeBrushInConstructionScript]]**(AVolume * Volume) |
| bool | **[[ShouldBuildShowWIP]]**() |
| bool | **[[ShouldUseLegacyFXSoundFunction]]**(UObject * WorldContextObject) |
| bool | **[[ShouldUseOpenLoadout]]**(UObject * WorldContextObject) |
| bool | **[[ShouldUsePIEJoinGameFlow]]**(UObject * WorldContextObject) |
| void | **[[SortActorArray]]**(TArray< AActor * > InActors, FActorSortDelegate SortDelegate, UObject * BoolContainer, FName BoolPropertyName, TArray< AActor * > & OutActors) |
| TArray< [FGameModeMessage](/docs/SDK/Source/Classes/structFGameModeMessage.md) > | **[[SortGameModeMessagesByPriority]]**(TArray< [FGameModeMessage](/docs/SDK/Source/Classes/structFGameModeMessage.md) > GameModeMessages) |
| TArray< [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * > | **[[SortPlayerStateArrayByPlayerKills]]**(TArray< [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * > PlayerStates) |
| TArray< [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * > | **[[SortPlayerStateArrayByPlayerScore]]**(TArray< [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * > PlayerStates) |
| TArray< [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * > | **[[SortPlayerStateArrayByPlayerScoreNoMatchBonus]]**(TArray< [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * > PlayerStates) |
| TArray< [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * > | **[[SortPlayerStateArrayByRecentlyJoined]]**(TArray< [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * > PlayerStates) |
| TArray< [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * > | **[[SortTeamArrayByScore]]**(TArray< [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * > Teams) |
| TArray< [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * > | **[[SortTeamArrayByTickets]]**(TArray< [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * > Teams) |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[SpawnAndDropInventoryItem]]**(UObject * WorldContextObject, TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > InventoryItemClass, FTransform SpawnTransform, [FDropItemParams](/docs/SDK/Source/Classes/structFDropItemParams.md) DropParams, FVector Impulse) |
| void | **[[StopSoundById]]**(int32 PlayingID) |
| void | **[[TBLApplyDamage]]**(AActor * DamagedActor, float Amount, [UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * DamageSource, AActor * DamageCauser, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * InventoryItem, bool bOverrideImpactPoint, FVector ImpactPointOverride, AActor * DamageInstigator, bool CheckForValidDamageSource) |
| void | **[[TBLSetEquippedItemsOnFire]]**(AActor * Actor, float Amount, [UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * DamageSource) |
| | **[[UTBLSystemLibrary]]**() |
| void | **[[UpdateActorsTags]]**(AActor * Actor, TArray< FName > Tags, UObject * WorldContextObject) |
| bool | **[[WasRecentlyRenderedOnScreen]]**(AActor * InActor, float InTolerance) |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200