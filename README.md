**You must include the following in (a) any copy or distribution of this dataset or portion of this data set, (b) any Derivation (defined below) of this dataset or portion of this data set, or (c) any new data set or work that extracts from or modifies this data set or portion of this data set in any way:**

**Ownership and License.** This data set is owned by ANDRO Computational Solutions, LLC (https://www.androcs.com/) and is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) located at https://creativecommons.org/licenses/by-nc-sa/4.0/  (the “Creative Commons License”)

**Attribution.** You must prominently display ANDRO Computational Solutions, LLC and the ANDRO logo: ![ANDRO](https://github.com/ANDROComputationalSolutions/RadarCommDataset/blob/main/ANDRO_textLogo_tagline3_h100white.png)
 
**Derivations.** “Derivations” means that you create a new work or new data set that aggregates this data set or any portion of this dataset, uses this data set or any portion of this  for any calculations, and/or is derived from or is based on this data set or any portion of this dataset.  

# RadarCommDataset: Radar & Communication signals Dataset
> **RadarCommDataset is a wireless signal dataset released for public use under the [Creative Commons Attribution - NonCommercial - ShareAlike 4.0 (CC BY-NC-SA 4.0) License](https://creativecommons.org/licenses/by-nc-sa/4.0/). The lack of existing multitask labelled datasets for machine learning for wireless communication is the prime motivation urging this release. RadarCommDataset is first of its kind multitask labelled dataset released to help research community to advance machine learning for wireless communication. The dataset contains radar and communication waveforms. This repository supplements helper scripts to visualize as well as extract the dataset.**
## Download link
https://drive.google.com/file/d/1U9pFFlA85Gb4OQSHAkoppEWswsN10PGD/view?usp=sharing
## Contributors
* Anu Jagannath    - ajagannath@androcs.com - Marconi Rosenblatt AI/ML Innovation Lab
* Jithin Jagannath - jjagannath@androcs.com - Marconi Rosenblatt AI/ML Innovation Lab

## Format description
* Type - HDF5
* Key  - {modulation,signal,snr,sample}
* Tensor - 256 x 1 - {inphase of length 128, quadrature of length 128}
* Sampling rate - 10 MS/s
* Total snapshots per waveform - 700
* SNR range - -20 dB to 18 dB in steps of 2 dB
* Modulation Classes - Pulsed Continuous wave, Frequency modulated Continuous wave, BPSK, AM-DSB, AM-SSB, ASK
* Signal Classes -  Airborne detection radar, Airborne range radar, Air-Ground MTI radar, Ground mapping radar, Radar Altimeter, SATCOM, AM Radio, Short-range wireless

## Waveform Generation
* Platform - GNURadio Companion
* Dynamic effects - Dynamic channel model GRC block (gnuradio.channels.dynamic_channel_model) over range of SNRs
## Helper Scripts Usage
* load_dataset.py - script to load the dataset
* visualize.py    - script to visualize specified waveform

## How to cite this dataset ? Please cite the original paper.
* **BibTeX** 
> >  @article{JagannathMTL,
  title={{Multi-task Learning Approach for Automatic Modulation and Wireless Signal Classification}},
  author={Jagannath, Anu and Jagannath, Jithin},
  journal={arXiv preprint},
  year={2021}
} </br >
* **Plain Text** 
> > A. Jagannath and J. Jagannath. "Multi-task Learning Approach for Automatic Modulation and Wireless Signal Classification", arXiv preprint, Nov 2021.</br >

