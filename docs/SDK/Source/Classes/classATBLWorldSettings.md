---
title: ATBLWorldSettings
type: class
aliases: ATBLWorldSettings
share: false

---

# ATBLWorldSettings





Inherits from AWorldSettings

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ATBLWorldSettings]]**() |
| TMap< [ASpawner](/docs/SDK/Source/Classes/classASpawner.md) *, FString > | **[[GetSpawnerSequenceBindingPrefixes]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TSoftObjectPtr< ALevelSequenceActor > | **[[AgathaDefeatSequence]]**  |
| TSoftObjectPtr< ALevelSequenceActor > | **[[AgathaVictorySequence]]**  |
| TSubclassOf< [ATBLActor](/docs/SDK/Source/Classes/classATBLActor.md) > | **[[AlwaysOnMusicManagerClass]]**  |
| [ASpawner](/docs/SDK/Source/Classes/classASpawner.md) * | **[[AttackerInitialSpawn]]**  |
| TSoftObjectPtr< ALevelSequenceActor > | **[[AttackerWarmupSequence]]**  |
| EFaction | **[[AttackingFaction]]**  |
| bool | **[[BlockLoadoutSelectionInClassSelectScreen]]**  |
| TSoftObjectPtr< ALevelSequenceActor > | **[[BlueSequence]]**  |
| float | **[[DefaultContextVoFrequencyPerMin]]**  |
| int32 | **[[DefaultContextVoNumPlayers]]**  |
| FName | **[[DefaultSpecialEventLevel]]**  |
| [ASpawner](/docs/SDK/Source/Classes/classASpawner.md) * | **[[DefenderInitialSpawn]]**  |
| TSoftObjectPtr< ALevelSequenceActor > | **[[DefenderWarmupSequence]]**  |
| EFaction | **[[DefendingFaction]]**  |
| bool | **[[DisableFallState]]**  |
| bool | **[[DisableSpectatorInTeamSelect]]**  |
| TSoftObjectPtr< ALevelSequenceActor > | **[[EpilogueSequence]]**  |
| UDataTable * | **[[GameModeMessageTable]]**  |
| [UTBLGameModeSettings](/docs/SDK/Source/Classes/classUTBLGameModeSettings.md) * | **[[GameModeSettings]]**  |
| TEnumAsByte< EGameModeType::Type > | **[[GamemodeType]]**  |
| FText | **[[MapDescription]]**  |
| FText | **[[MapName]]**  |
| [UTBLMapSummary](/docs/SDK/Source/Classes/classUTBLMapSummary.md) * | **[[MapSummary]]**  |
| TSoftObjectPtr< ALevelSequenceActor > | **[[MasonDefeatSequence]]**  |
| TSoftObjectPtr< ALevelSequenceActor > | **[[MasonVictorySequence]]**  |
| FName | **[[PodiumSublevel]]**  |
| float | **[[PodiumTime]]**  |
| TSoftObjectPtr< ALevelSequenceActor > | **[[PreparingMatchSequence]]**  |
| TSoftObjectPtr< ALevelSequenceActor > | **[[PrologueSequence]]**  |
| TSoftObjectPtr< ALevelSequenceActor > | **[[RedSequence]]**  |
| TMap< TSoftObjectPtr< [ASpawner](/docs/SDK/Source/Classes/classASpawner.md) >, FString > | **[[SpawnerSequenceBindingPrefixes]]**  |
| TArray< [FSpecialEventLevelEntry](/docs/SDK/Source/Classes/structFSpecialEventLevelEntry.md) > | **[[SpecialEventStreamingLevels]]**  |
| [FStageEndingConfig](/docs/SDK/Source/Classes/structFStageEndingConfig.md) | **[[StageEndingConfig]]**  |
| FName | **[[StatsOverrideRowName]]**  |
| [FStageEndingConfig](/docs/SDK/Source/Classes/structFStageEndingConfig.md) | **[[TenosiaCompatibleStageEndingConfig]]**  |
| bool | **[[UseNewStageIdNumbers]]**  |
| TSoftObjectPtr< ALevelSequenceActor > | **[[VictoryPodiumSequence]]**  |
| TSoftObjectPtr< ALevelSequenceActor > | **[[WaitingForPlayersSequence]]**  |
| bool | **[[bBotsShouldAlwaysCheckFloor]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200