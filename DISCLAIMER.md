# Corporate AV Testing & Calibration Toolkit EULA & Disclaimer

This Corporate AV Testing & Calibration Toolkit (hereafter "the Software"), including all interactive web pages, audio generators, calibration graphics, video clips, checklists, guides, and Python scripts, is provided in good faith for system validation, education, and tuning purposes.

## 1. Terms of Use
By downloading, running, copying, or utilizing any portion of the Software, you agree to be bound by the terms of this End-User License Agreement (EULA). If you do not agree to these terms, do not use the Software.

## 2. Disclaimer of Warranties (No Warranty)
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## 3. Limitation of Liability
IN NO EVENT SHALL THE DEVELOPER OR CONTIBUTORS BE LIABLE FOR ANY DAMAGES WHATSOEVER (INCLUDING, WITHOUT LIMITATION, DAMAGES FOR LOSS OF BUSINESS PROFITS, BUSINESS INTERRUPTION, LOSS OF BUSINESS INFORMATION, AUDIO GEAR DAMAGE, HEARING DAMAGE, NETWORK DOWN-TIME, OR ANY OTHER PECUNIARY LOSS) ARISING OUT OF THE USE OF OR INABILITY TO USE THIS PRODUCT, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

## 4. Critical Operational Warnings
*   **Acoustic Risk:** High-volume reference tones (especially the 1 kHz ref tone) and frequency sweeps (20 Hz - 20 kHz) can cause permanent hearing damage or blow out loudspeaker drivers (high-frequency tweeters or subwoofers). Always start tests with system volumes at minimum and increase gain incrementally.
*   **Network Risk:** Diagnostic scripts (such as `network_av_diagnostics.py`) run active pings and latency probes. Do not run these on secure or production enterprise networks without proper administrative permissions and monitoring.
*   **Display Burn-In Risk:** High-contrast calibration patterns (alignment grids, color bars, screen share text legibility charts) can cause permanent screen burn-in on OLED, CRT, or plasma displays if left static for extended periods. Do not leave calibration patterns active unattended.

---
*Date of Document: June 2026*
