<a name="readme-top"></a>

<div align="center">
  <img src="https://raw.githubusercontent.com/reitwiec/openPSD/refs/heads/master/static/img/logo.png" alt="Logo" width="200">
  <h1 align="center" style="border-bottom: none">Open Pressure Sensing Device: Measure tactile pressure thresholds digitally</h1>
</div>

<div align="center">
  <a href=""><img src="https://img.shields.io/badge/LICENSE-MIT-20B2AA?style=for-the-badge" alt="MIT License"></a>
  <br/>
  <a href=""><img src="https://img.shields.io/badge/Documentation-000?logo=googledocs&logoColor=FFE165&style=for-the-badge" alt="Check out the documentation"></a>
</div>

<hr>

Welcome to OpenPSD, a handheld, open-source instrument designed to measure tactile pressure thresholds digitally. Adapted from clinical tools like the AcroVal™ system, it applies calibrated pressure to the skin and records sensory responses for studies of nerve regeneration following reconstructive surgery.

[Check out the docs]()

### OpenPSD History
This project supports the ongoing research of [Dr. David Otterburn](https://www.otterburnlab.org/) and Carson Gundlach at Weill Cornell Medicine, whose work in neurotization seeks to restore sensory nerve connections following breast reconstruction surgery.

After mastectomy, patients often experience a loss of sensation that affects comfort, safety, and quality of life. Through surgical co-aptation of donor and recipient nerves, Dr. Otterburn’s team aims to re-establish sensory pathways; however, evaluating the success of that process has long relied on subjective or coarse analog tools.

Developed by Cornell Tech Master’s students [Michelle Hui](https://michelle-hui.com/) and [Reitwiec Shandilya](https://www.linkedin.com/in/reitwiec/), this open-source device captures quantitative measurements of tactile pressure. By precisely logging patient response data, it allows clinicians to objectively track sensory recovery over time, providing richer, reproducible data than traditional Semmes-Weinstein monofilaments, which only measure at discrete force intervals. Beyond reconstructive surgery, the same sensing tool could inform other clinical neurological testing and research functions, expanding open-source tools for quantifying sensation and nerve function.

The project is supported by the Cornell Tech [MakerLab](https://tech.cornell.edu/research/makerlab/) and is undertaken in partnership with the [Open Source Hardware Association’s](https://oshwa.org/) [Open Healthware Initiative](https://oshwa.org/announcements/oshwas-new-open-healthware-certification-how-we-got-here-and-where-were/), with the support of the National Science Foundation. The goal is to create a validated, open-source alternative to proprietary devices such as the AcroVal™ Neurosensory & Motor Testing System, enabling wider adoption of transparent, reproducible clinical instrumentation across research and education.

![Pressure Monitor](https://img.shields.io/badge/Platform-macOS-blue) ![Electron](https://img.shields.io/badge/Electron-31-green) ![React](https://img.shields.io/badge/React-18-blue)

### OpenPSD Features
- **Real-time pressure readings** via USB serial connection
- **Session management** - Create, view, and export patient sessions
- **Historical trend visualization** - Track pressure changes across sessions
- **Device calibration** - Built-in calibration workflow
- **CSV export** - Export sessions for external analysis
- **Offline operation** - All data is stored locally

### OpenPSD Build
We designed openPSD with the intention that anyone should be able to build it using commonly accessible parts. This principle guided our design decisions and ultimately influenced the form and shape of the device.

[Check out on Instructables]()


### Everything Else
Feel free to [open up an issue](https://github.com/reitwiec/openPSD/issues) if there's something you'd like to see!

Hear us talk about OpenPSD on [The CircuitPython Show]()!

All our work is available under the MIT License - See LICENSE file for details.
