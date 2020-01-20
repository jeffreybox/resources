<a name='Top'></a>
# ACS MANAGED DEVICES
Dataset Report

v0.1

Burak Akoguz (burak.akoguz@cox.com)

COX Communications

## TABLE OF CONTENTS
- [DESCRIPTION](#Description)
- [DATA DICTIONARY](#Data_Dictionary)
- [MINERVA vs AWS](#Minerva_vs_AWS)
- [BASIC STATISTICS](#Basic_Statistics)
- [DATA SAMPLES](#Data_Samples)
- [DATA QUALITY](#Data_Quality)
- [NOTES](#Notes)
- [QUESTIONS](#Questions)

<br>
<a name='Description'></a>

## DESCRIPTION
[Top](#Top)
<br>

This report reflects the properties of the ACS (Auto-Configuration System) Managed
Devices dataset present in AWS S3 location accessible through queries from AWS
Athena and/or Hive/SparkQL. The details or accessing this dataset is:

| Property     | Value                  |
|--------------|------------------------|
| Database     | acs                    |
| Table        | prfrm_mtrc_mngdvc_hrly |
| Path         | [s3://cci-edo-data-source/raw/acs/prfrm_mtrc_mngdvc_hrly](https://console.aws.amazon.com/s3/buckets/cci-edo-data-source/raw/acs/prfrm_mtrc_mngdvc_hrly/?region=us-east-1) |
| Glue Catalog | [prfrm_mtrc_mngdvc_hrly](https://us-east-1.console.aws.amazon.com/glue/home?region=us-east-1#table:name=prfrm_mtrc_mngdvc_hrly;namespace=acs) |
| File Type    | ORC                    |
| Total Record | 49234720997 (49.23B)   |
| Partioned By | dt, hour_of_day        |

<br>
<a name='Data_Dictionary'></a>

## DATA DICTIONARY
[Top](#Top)
<br>

| Column                   | Data Type   | Meaning                                                                                   | Purpose                                                                                   |
|--------------------------|-------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| cpeid                    | string      | Customer Premise Equipment Id                                                             | Identifies customer                                                                       |
| serial_number            | string      | Serial Number of the device                                                               | Mostly same as cpeid                                                                      |
| mac_address              | string      | Mac Address of the device                                                                 | MAC Address of the device (without : )                                                    |
| src_timestamp            | string      | Timestamp obtained from device                                                            | Time of the source device when data gathered                                              |
| interface_id             | string      | Interface ID                                                                              | Devices can have more than one service profiles (or SSIDs)                                |
| ssid                     | string      | The current service set identifier in use by the connection                               | Name of the Access Point                                                                  |
| bssid                    | string      | Basic Service Set Identifier                                                              | Access point mac address (useful when same SSID from different modems)                    |
| radio_enabled            | string      | Indicates whether or not the access point radio is enabled.                               |                                                                                           |
| standard                 | string      | Indicates which IEEE 802.11 standard this WLANConfiguration instance is configured for    | Enumeration of: a, b, g (b and g clients supported), g-only (only g clients supported), n |
| fallback_enabled         | string      | ??? Alternative Access to the internet                                                    | Sometimes used for alternative ways to connect like 4G                                    |
| enabled                  | string      | Enables or disables this interface                                                        | 0 or 1 (mostly 0 ???)                                                                     |
| status                   | string      | Indicates the status of this interface                                                    | Enumeration of: Up, Error (OPTIONAL), Disabled                                            |
| max_bit_rate             | bigint      | The maximum upstream and downstream bit rate available to this connection in Mbps.        | Either Auto, or the largest of the OperationalDataTransmitRates values.                   |
| bytes_received           | bigint      | The total number of bytes received on the interface, including framing characters.        | Ethernet only                                                                             |
| total_bytes_received     | bigint      | The total number of bytes received on the interface, including framing characters.        |                                                                                           |
| packets_received         | bigint      | The total number of packets which were received on this interface.                        | Ethernet only                                                                             |
| total_packets_received   | bigint      | The total number of packets which were received on this interface.                        |                                                                                           |
| bytes_sent               | bigint      | The total number of bytes transmitted out of the interface, including framing characters. | Ethernet only                                                                             |
| total_bytes_sent         | bigint      | The total number of bytes transmitted out of the interface, including framing characters. |                                                                                           |
| packets_sent             | bigint      | The total number of packets transmitted out of the interface.                             | Ethernet only                                                                             |
| total_packets_sent       | bigint      | The total number of packets transmitted out of the interface.                             |                                                                                           |
| received_dropped         | bigint      | ???                                                                                       |                                                                                           |
| received_errored         | bigint      | ???                                                                                       |                                                                                           |
| sent_dropped             | bigint      | ???                                                                                       |                                                                                           |
| sent_errored             | bigint      | ???                                                                                       |                                                                                           |
| dt                       | string      | Date based on days                                                                        | Shows the day of the record                                                               |
| hour_of_day              | string      | Hours of the day                                                                          | Shows hourly records in a day for devices                                                 |

<br>
<a name='Minerva_vs_AWS'></a>

## MINERVA vs AWS
[Top](#Top)
<br>

In this section there will be some comparison metrics will be given to check
the data quality between Minerva and AWS data sources for the same dataset.

| AWS/Minerva | Db.Table                       | Row Cnt                | Min(dt)     | Max(dt)     |
|-------------|--------------------------------|------------------------|-------------|-------------|
| AWS         | acs.prfrm_mtrc_mngdvc_hrly     | 49234720997 (49.23B)   | 2018-01-02  | 2019-01-31  |
| AWS         | acs.acs_prfrm_mtrc_mngdvc_hrly | 68684118672 (68.68B)   | 2017-10-31  | 2019-07-02  |
| Minerva     | acs.acs_prfrm_mtrc_mngdvc_hrly | 68706197152 (68.70B)   | 2017-09-10  | 2019-07-03  |

### 1. Record Count vs Date
| AWS (acs.prfrm_mtrc_mngdvc_hrly)                                  | AWS (acs.acs_prfrm_mtrc_mngdvc_hrly)                                                                  | MINERVA (acs.acs_prfrm_mtrc_mngdvc_hrly)                                       |
|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| ![Record Count vs Date](cnt_VS_dt.png)                            | ![Record Count vs Date](aws_acs.acs_prfrm_mtrc_mngdvc_hrly__cnt_VS_dt.png)                            | ![Record Count vs Date](minerva_acs.acs_prfrm_mtrc_mngdvc_hrly__cnt_VS_dt.png) |

### 2. Record Count per CPEID vs Date
| AWS (acs.prfrm_mtrc_mngdvc_hrly)                                  | AWS (acs.acs_prfrm_mtrc_mngdvc_hrly)                                                                  | MINERVA (acs.acs_prfrm_mtrc_mngdvc_hrly)                                       |
|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| ![Record Count per CPEID vs Date ](cnt_per_cpeid_VS_dt.png)       | ![Record Count per CPEID vs Date ](aws_acs.acs_prfrm_mtrc_mngdvc_hrly__cnt_per_cpeid_VS_dt.png)       | ![Record Count per CPEID vs Date ](minerva_acs.acs_prfrm_mtrc_mngdvc_hrly__cnt_per_cpeid_VS_dt.png) |

### 3. Distinct CPEID Count vs Date
| AWS (acs.prfrm_mtrc_mngdvc_hrly)                                  | AWS (acs.acs_prfrm_mtrc_mngdvc_hrly)                                                                  | MINERVA (acs.acs_prfrm_mtrc_mngdvc_hrly)                                      |
|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| ![Distinct Devices Count vs Date ](dist_cpeid_cnt_VS_dt.png)      | ![Distinct Devices Count vs Date ](aws_acs.acs_prfrm_mtrc_mngdvc_hrly__dist_cpeid_cnt_VS_dt.png)      | ![Distinct Devices Count vs Date ](minerva_acs.acs_prfrm_mtrc_mngdvc_hrly__dist_cpeid_cnt_VS_dt.png) |

### 4. Distinct Hours Count vs Date
| AWS (acs.prfrm_mtrc_mngdvc_hrly)                                  | AWS (acs.acs_prfrm_mtrc_mngdvc_hrly)                                                                  | MINERVA (acs.acs_prfrm_mtrc_mngdvc_hrly)                                      |
|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| ![Distinct Hours Count vs Date ](dist_hour_cnt_VS_dt.png)         | ![Distinct Hours Count vs Date ](aws_acs.acs_prfrm_mtrc_mngdvc_hrly__dist_hour_cnt_VS_dt.png)         | ![Distinct Hours Count vs Date ](minerva_acs.acs_prfrm_mtrc_mngdvc_hrly__dist_hour_cnt_VS_dt.png)   |

### 5. Average Count Distinct Hours vs Date
| AWS (acs.prfrm_mtrc_mngdvc_hrly)                                  | AWS (acs.acs_prfrm_mtrc_mngdvc_hrly)                                                                  | MINERVA (acs.acs_prfrm_mtrc_mngdvc_hrly)                                      |
|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| ![Avg_Count_Distinct Hours vs Date ](avg_cnt_dist_hour_VS_dt.png) | ![Avg_Count_Distinct Hours vs Date ](aws_acs.acs_prfrm_mtrc_mngdvc_hrly__avg_cnt_dist_hour_VS_dt.png) | ![Avg_Count_Distinct Hours vs Date ](minerva_acs.acs_prfrm_mtrc_mngdvc_hrly__avg_cnt_dist_hour_VS_dt.png)   |


<br>
<a name='Basic_Statistics'></a>

## BASIC STATISTICS
[Top](#Top)
<br>

| Column                 | Data Type | Min                          | Max              | Mean         | Median |
|------------------------|-----------|------------------------------|------------------|--------------|--------|
| cpeid                  | string    | ""                           | f45fd4c1cbaa     | N/A          | N/A    |
| serial_number          | string    | ""                           | serial_number    | N/A          | N/A    |
| mac_address            | string    | ""                           | mac_address      | N/A          | N/A    |
| src_timestamp          | string    | 2018-01-02 00:18:48 UTC+0000 | timestamp        | N/A          | N/A    |
| interface_id           | string    | 1                            | interface_id     | N/A          | N/A    |
| ssid                   | string    | ""                           | �	���B�d�#:�     | N/A          | N/A    |
| bssid                  | string    | ""                           | } - Network"     | N/A          | N/A    |
| radio_enabled          | string    | ""                           | ttp://ciafbi"    | N/A          | N/A    |
| standard               | string    | ""                           | x                | N/A          | N/A    |
| fallback_enabled       | string    | ""                           | false            | N/A          | N/A    |
| enabled                | string    | ""                           | xwPY5lMkNzMY     | N/A          | N/A    |
| status                 | string    | ""                           | yVQG9iYBWk31     | N/A          | N/A    |
| max_bit_rate           | bigint    | 0                            | 802              | 0.0049       |        |
| bytes_received         | bigint    | 0                            | 3963870476       | 2883.2476    |        |
| total_bytes_received   | bigint    | 0                            | 349965           | 0.0048       |        |
| packets_received       | bigint    | 0                            | 4259505728       | 408.3556     |        |
| total_packets_received | bigint    | 0                            | 1                | 8.2299E-8    |        |
| bytes_sent             | bigint    | 0                            | 4292065649       | 4264984.2285 |        |
| total_bytes_sent       | bigint    | 0                            | 989805313        | 26.6567      |        |
| packets_sent           | bigint    | 0                            | 2998329492       | 4224943.4545 |        |
| total_packets_sent     | bigint    | 0                            | 988429749        | 26.3239      |        |
| received_dropped       | bigint    | 0                            | 2129464992       | 425.9105     |        |
| received_errored       | bigint    | 0                            | 2168811887       | 2071.5559    |        |
| sent_dropped           | bigint    | 0                            | 2130689350       | 1194.7747    |        |
| sent_errored           | bigint    | 0                            | 2147483647       | 40457.3277   |        |
| dt                     | string    | 2018-01-02                   | 2019-01-31       | N/A          | N/A    |
| hour_of_day            | string    | 00                           | 23               | N/A          | N/A    |


<br>
<a name='Data_Samples'></a>

## DATA SAMPLES
[Top](#Top)
<br>

| Column                 | Data Type | Most Frequent Values                                                                     | Notes                         |
|------------------------|-----------|------------------------------------------------------------------------------------------|-------------------------------|
| cpeid                  | string    | 7822C26B2B05962, F7YBUL646317434, FABBUL758347979                                        | 15200 records ""              |
| serial_number          | string    | "", 7822C26B2B05962, F7YBUL646317434, FABBUL758347979                                    |   64M (0.13%) records ""      |
| mac_address            | string    | "", 18B81FB4B28F, 5C8FE058AF51, 5C8FE0E10DFC                                             |  3833 records ""              |
| src_timestamp          | string    | 2018-08-21 01:46:29 UTC+0000, 2018-07-19 08:48:58 UTC+0000, 2018-08-27 10:23:57 UTC+0000 | Uniformly distributed         |
| interface_id           | string    | 10001 to 10016                                                                           | Uniformly distributed         |
| ssid                   | string    | 000000, Home, FBI Surveillance Van, Guest, 2.4, Home2, FBI, Fast, Home1, Hogwarts        |  0.30M (0.00060%) records ""  |
| bssid                  | string    | 00:00:00:00:00:00, BE:2E:48:F1:99:EC, DE:2E:48:F1:99:EC                                  |  0.15M (0.00030%) records ""  |
| radio_enabled          | string    | "", true, false, radio_enabled, 38:70:0C:12:41:CD                                        | 48.51B (98.53%) records ""    |
| standard               | string    | 802.11, n, g, "", standard                                                               |  0.19M (0.00038%) records ""  |
| fallback_enabled       | string    | "", false, 801.11, fallback_enabled, -5G", ", 58:19:F8:D1:99:69                          | 48.51B (98.53%) records ""    |
| enabled                | string    | 0, 1, false, true, "", enabled                                                           |  0.19M (0.00038%) records ""  |
| status                 | string    | Down, Up, Disabled, "", 1, status, 801.11                                                |  0.16M (0.00032%) records ""  |
| max_bit_rate           | bigint    | "", 0, 1, 802                                                                            | 68.11B (98.31%) records null  |
| bytes_received         | bigint    | 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20                                                    | 46.93B (95.32%) records 0     |
| total_bytes_received   | bigint    | 0, "", 1, 802, 4, 2, 76, 8, 1302                                                         | 49.23B (99.99%) records 0     |
| packets_received       | bigint    | 0, "", 1, 716895750, 716895751                                                           | 49.23B (99.99%) records 0     |
| total_packets_received | bigint    | 0, "", 1                                                                                 | 49.23B (99.99%) records 0     |
| bytes_sent             | bigint    | 0, 5, 4, 6, 10, 3, 11                                                                    | 46.25B (93.94%) records 0     |
| total_bytes_sent       | bigint    | 0, "", 10, 934734, 5502400                                                               | 49.23B (99.99%) records 0     |
| packets_sent           | bigint    | 0, 5, 4, 6, 3, 10, 11, 2                                                                 | 46.44B (94.33%) records 0     |
| total_packets_sent     | bigint    | 0, "", 15255053                                                                          | 49.23B (99.99%) records 0     |
| received_dropped       | bigint    | 0, "", 726295924, 725394804                                                              | 49.23B (99.99%) records 0     |
| received_errored       | bigint    | 0, 2, 4, 6, 8, 10                                                                        | 46.93B (95.32%) records 0     |
| sent_dropped           | bigint    | 0, "", 2130238790, 2127424838, 2129288518, 2126273862, 4                                 | 49.23B (99.99%) records 0     |
| sent_errored           | bigint    | 0, 22, 21, 23, 24, 43, 25, 32, 42                                                        | 46.67B (94.79%) records 0     |
| dt                     | string    | 2018-08-20, 2018-08-21, 2018-12-24, 2018-09-27                                           | Uniformly distributed         |
| hour_of_day            | string    | 06, 00, 23, 01, 21                                                                       | Uniformly distributed         |


<br>
<a name='Data_Quality'></a>

## DATA QUALITY
[Top](#Top)
<br>

For the data quality checks, the amount of data logically in expected range versus
all data can be a good measure. The following table is showing this property for
all of the features (columns) in the dataset.
- 1. 49234720997 is the total number of rows
- 2. 13725 rows repeating header

| Column                 | Data Type | Unique Value Count | % Meaningful Data | % NNEZ* |
|------------------------|-----------|--------------------|-------------------|---------|
| cpeid                  | string    | 1726808            | 99.99             | 5.87E-5 |
| serial_number          | string    | 1724407            | 99.86             | 0.13    |
| mac_address            | string    | 1724408            | 99.86             | 0.13    |
| src_timestamp          | string    | 17666525           | 100               | 0.0     |
| interface_id           | string    | 25                 | 98.53             | 2.78E-5 |
| ssid                   | string    | 5127517            | 99.99             | 6.80E-4 |
| bssid                  | string    | 26983976           | 99.99             | 3.46E-4 |
| radio_enabled          | string    | 56                 | 1.46              | 98.53   |
| standard               | string    | 21                 | 99.99             | 4.24E-4 |
| fallback_enabled       | string    | 7                  | 1.46              | 98.53   |
| enabled                | string    | 17                 | 98.53             | 4.27E-4 |
| status                 | string    | 16                 | 98.71             | 3.60E-4 |
| max_bit_rate           | bigint    | 3                  | 3.20E-5           | 99.99   |
| bytes_received         | bigint    | 1754737            | 4.67              | 95.32   |
| total_bytes_received   | bigint    | 3745               | 5.20E-5           | 99.99   |
| packets_received       | bigint    | 7592               | 6.61E-5           | 99.99   |
| total_packets_received | bigint    | 2                  | 8.22E-6           | 99.99   |
| bytes_sent             | bigint    | 396982289          | 6.04              | 93.95   |
| total_bytes_sent       | bigint    | 22371              | 4.67E-5           | 99.99   |
| packets_sent           | bigint    | 391865977          | 5.66              | 94.33   |
| total_packets_sent     | bigint    | 17909              | 4.45E-5           | 99.99   |
| received_dropped       | bigint    | 4371               | 6.49E-5           | 99.99   |
| received_errored       | bigint    | 1745493            | 4.67              | 95.32   |
| sent_dropped           | bigint    | 6691               | 9.48E-5           | 99.99   |
| sent_errored           | bigint    | 18130004           | 5.19              | 94.80   |
| dt                     | string    | 358                | 99.99             | 2.78E-5 |
| hour_of_day            | string    | 24                 | 99.99             | 2.78E-5 |

- \* Null, None and Empty check for strings, Null and Zero check for numbers
- For "enabled", 0 could mean something so NNEZ value doesn't include 0

<br>
<a name='Notes'></a>

## NOTES
[Top](#Top)
<br>

- After 2019-03-01, there is a degradation in data. The number of distinct cpeid per day for different regions can be seeen in the following graphics.

![Count Distinct CPEID](cnt_dist_cpeid_VS_dt_by_site_id_1.png)
![Count Distinct CPEID](cnt_dist_cpeid_VS_dt_by_site_id_2.png)
![Count Distinct CPEID](cnt_dist_cpeid_VS_dt_by_site_id_3.png)

- For 98.41% of data, cpeid=serial_number
- 90319729 (90M) times interface_id is 1 (normally between 10001 and 10016)
- cpeid mostly capital letters, when interface_id in (1-16) then cpeid has lower case letters
- cpeid="72N2T7692B02689" gives strange ssid, no bssid, and radio_enabled (http link)
- 95.28% of the devices have ARRIS in the SSID field (most probably ARRIS brand)
- if we apply filters to get more meaningful data:

  | Column                 | Data Type | Min                          | Max                          | Mean         | Median |
  |------------------------|-----------|------------------------------|------------------------------|--------------|--------|
  | cpeid                  | string    | 6AX2ULACC307153              | GAUBULACC397251              | N/A          | N/A    |
  | serial_number          | string    | 4C316A73A0272                | GAUBULACC397251              | N/A          | N/A    |
  | mac_address            | string    | 044E5AA6AFE6                 | FFFFFFFFFFF                  | N/A          | N/A    |
  | src_timestamp          | string    | 2018-01-02 00:18:48 UTC+0000 | 2019-01-31 23:59:59 UTC+0000 | N/A          | N/A    |
  | interface_id           | string    | 10001                        | 10016                        | N/A          | N/A    |
  | ssid                   | string    | ""                           | \~\~\~\~\~\~\~               | N/A          | N/A    |
  | bssid                  | string    | 00:00:00:00:00:00            | FE:CA:B5:F1:4C:B5            | N/A          | N/A    |
  | radio_enabled          | string    | false                        | true                         | N/A          | N/A    |
  | standard               | string    | 802.11                       | g                            | N/A          | N/A    |
  | fallback_enabled       | string    | ""                           | false                        | N/A          | N/A    |
  | enabled                | string    | 0                            | 1                            | N/A          | N/A    |
  | status                 | string    | Disabled                     | Up                           | N/A          | N/A    |
  | max_bit_rate           | bigint    | 0                            | 802                          | 202.7049     |        |
  | bytes_received         | bigint    | 0                            | 3963870476                   | 2926.3576    |        |
  | total_bytes_received   | bigint    | 0                            | 349965                       | 0.0049       |        |
  | packets_received       | bigint    | 0                            | 4259505728                   | 414.8267     |        |
  | total_packets_received | bigint    | 0                            | 1                            | 8.3627E-8    |        |
  | bytes_sent             | bigint    | 0                            | 4292065649                   | 4327601.7090 |        |
  | total_bytes_sent       | bigint    | 0                            | 989805313                    | 27.0869      |        |
  | packets_sent           | bigint    | 0                            | 2998329492                   | 4286971.7620 |        |
  | total_packets_sent     | bigint    | 0                            | 988429749                    | 26.7487      |        |
  | received_dropped       | bigint    | 0                            | 2129464992                   | 432.6640     |        |
  | received_errored       | bigint    | 0                            | 2168811887                   | 2101.8055    |        |
  | sent_dropped           | bigint    | 0                            | 2130689350                   | 1213.7048    |        |
  | sent_errored           | bigint    | 0                            | 2147483647                   | 41052.8589   |        |
  | dt                     | string    | 2018-01-02                   | 2019-01-31                   | N/A          | N/A    |
  | hour_of_day            | string    | 00                           | 23                           | N/A          | N/A    |

For ARRIS devices:
- Mostly 16 interfaces (one for 2G, one for 5G, one for GUEST)
- Bytes_received has value but total_bytes_received 0.
- Interface_id is between 10001 and 10016
- Even we have bytes_received > 0, packets_received is 0 (also
  total_packets_received)
- For bytes_received > 0, almost all the cases received_errored =
  bytes_received
- received_dropped is always 0
- bytes_sent has positive value for active interfaces, and when
  bytes_sent positive total_bytes_sent is always 0
- bytes_sent has positive value for active interfaces, and when
  bytes_sent positive packets_sent is ~91% positive (very close value
  to bytes_sent) 
- pockets_sent > 0 for active interfaces, but total_packets_sent is 0
- sent_dropped is always 0
- sent_errored has lower or equal value to bytes_sent


<br>
<a name='Questions'></a>

## QUESTIONS
[Top](#Top)
<br>
There are some questions about this dataset should be addressed by the owners of this dataset.


| Nr   | Pri  | Question                                                                             | Query   | Data   |
| ---- | ---- | ------------------------------------------------------------------------------------ | ------- | ------------- |
| 1    | Maj  | After 2019-03-01 there is a degradation in the data. Daily counts are almost 1/3 of the values previously. What is the reason for this change? | | See [MINERVA vs AWS](#Minerva_vs_AWS) Part 3 Middle graphic. |
| 2    | Maj  | For each cpeids, number of hours data present per day is around 3 before 2018-07 and 10 after this date (till degradation). We were expecting this number as 24. What is the reason for the difference? | | See [MINERVA vs AWS](#Minerva_vs_AWS) Part 5 |
| 3    | Maj  | For most of the numeric fields, the values more than 94% are 0.  Is it normal behaviour? | | See table in [DATA QUALITY](#Data_Quality) |
| 4    | Min  | It seeems header row is repeated for 13k times in the dataset. What is the reason for repeated header row? | ``` select count(*) from acs.prfrm_mtrc_mngdvc_hrly where cpeid='cpeid' ``` | 13725 |
| 5    | Min  | serial_number is the same as cpeid for almost all the time (98.41%). Is it normal?            | ``` select count(*)*100.0/49234720997 from acs.prfrm_mtrc_mngdvc_hrly where cpeid=serial_number ``` | 98.41(%) |
| 6    | Min  | mac_address does not include ":". What is the reason for that?                       | ``` select mac_address from acs.prfrm_mtrc_mngdvc_hrly limit 1 ``` | FC51A47B1040 |
| 7    | Min  | For interface_id, mostly values are in the range of 10001 to 10016. (1.46% of the values are not in this range.) Is it expected behaviour? | ``` select count(*)*100.0/49234720997 from acs.prfrm_mtrc_mngdvc_hrly where interface_id not in ('10001', '10002', '10003', '10004', '10005', '10006', '10007', '10008', '10009', '10010', '10011', '10012', '10013', '10014', '10015', '10016') limit 1 ``` | 1.46(%) |
| 8    | Min  | For max_bit_rate, values are in between 0 and 802 and data type is bigint. Is it normal? | ``` select min(max_bit_rate), max(max_bit_rate) from acs.prfrm_mtrc_mngdvc_hrly ``` | 0, 802  |
| 9    | Min  | For total_packets_received, values are 0 and 1 and data type is bigint. Is it normal? | ``` select distinct(total_packets_received) from acs.prfrm_mtrc_mngdvc_hrly ``` | 0, "", 1 |
