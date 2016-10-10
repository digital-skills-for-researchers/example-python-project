# NLDL Raw Data

Each raw data file contains both a set of readings and some relevant metadata. The files do not contain column headers.

- **Column A:** Metadata key
- **Column B:** Metadata value
- **Column C:** _unused_
- **Column D:** Elapsed Time (seconds) relative to time of stimulation
- **Column E:** Voltage recorded (V)


## Metadata Values

The following values are available from columns A&B of each raw data file:

- **Record Length**<br>
  Total number of data points recorded in the file.<br>
  _eg. 2500_

- **Sample Interval (s)**<br>
  Sampling frequency: the amount of time between each data point being created.<br>
  _eg. 0.000001_

- **Trigger Point**<br>
  Number of data points included as a recording buffer before the stimulus was applied.<br>
  _eg. 240_ (240 data points)


- **Oscilloscope Settings**<br>
  The oscilloscope settings were used during the recording, consisting of:

  - **Source**<br>
    The oscilloscope channel used to record.<br>
    _eg. CH1 (Channel 1)_

  - **Vertical Units**<br>
    Unit of measurement for the field potential. Does not take into account the amplification prior to the oscilloscope.<br>
    _eg. V (voltage)_

  - **Vertical Scale**<br>
    The sensitivity of the voltage readings, the resolution of the measurement (ie. smallest difference in voltage that was recorded)<br>
    _eg. 0.2_

  - **Vertical Offset (V)**<br>
    The reference voltage offset, which all other voltage measurements are relative to. This is not relevant for the final readings in the data set.<br>
    _eg. 0.264 (voltage)_

  - **Horizontal Units**<br>
    The unit of measure for the horizontal component of all readings.<br>
    _eg: s (seconds)_

  - **Horizontal Scale**<br>
    Size of the data frame visible on the oscilloscope.<br>
    _eg. 0.00025_

  - **Pt Fmt**<br>
    FMT stands for Frequency Mask Trigger which is the ability to do event-based capture. This tells the oscilloscope to keep a time window of pre-stimulus data as part of the trace.<br>
    _eg. Y (Yes)_

  - **Yzero**<br>
    Not sure... hopefully not relevant.<br>
    eg. 0

  - **Probe Atten**<br>
    The probe attenuation setting.<br>
    _eg. 10 (Ten times multiplier)_

  - **Firmware Version**<br>
    The oscilloscope's firmware version at the time of recording.
    _Value: FV:v6.08_




## Hand-Noted Metadata for TEK0000.CSV

Here is an example of the additional hand-recorded metadata for the first file TEK0000.CSV. This metadata has been digitized from notebook _"ZFinch Auditory Physiology - Slice feb '03 - MFK"_. Metadata like this is available from the physical notebook for every data file.

```
Bird: ZF04-72
Species: Zebra Finch
Sex: Male
Date: 10 April 2004
Experimentors: Fabiana Kubke, Rick Hyson
Slicing Procedure: Standard Slicing Procedure (documented separately)
Bath Temp: 30.6 C
Recording Electrode: Glass Electrode, manually broken tip filled with ACSF
Stimulating Electrode Position: midline
Stimulus: 20% of IM Amp
Filtering: Low-pass 10kHz
Recording Electrode Position (relative): x=14, y=19.7 
Slice #: 1
A-P Position: More rostral than Slice #2

Notes: Recording from Nucleus Laminaris
Data Generated: 11:17:56
Slice loaded with FITC/DA: 4pm
```






### Avoiding Pseudo-Replication and Invalid Comparisons

For each bird there are one or more slices. For each slice there are several recordings; there may be a data for more than one Stimulating Electrode Position per slice (ie. there may be more than one recording sequence for each slice).

The four variables are:
- Bird number
- Slice number
- Stimulating Electrode Position
- Recording Electrode Position

Look at repeats within the variables to avoid pseudo-replication.



Metadata created October 16th 2016 by T. Gray and F. Kubke