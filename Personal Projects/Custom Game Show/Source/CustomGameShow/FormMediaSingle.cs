/********************************
 * Custom Game Show
 * FormMediaSingle.cs
 * Created by Justin Leonard
********************************/

using System;
using System.Drawing;
using System.IO;
using System.Windows.Forms;

namespace CustomGameShow
{
    public partial class FormMediaSingle : Form
    {
        /*
         * Types
         */
        
        public enum MediaName
        {
            DynamicCustom0,
            DynamicCustom1,
            DynamicCustom2,
            DynamicCustom3,
            DynamicCustom4,
            DynamicCustom5,
            DynamicCustom6,
            DynamicCustom7,
            DynamicCustom8,
            DynamicCustom9,
            DynamicCustom10,
            DynamicCustom11,
            DynamicCustom12,
            DynamicCustom13,
            FinaleWinner0,
            FinaleWinner1,
            FinaleWinner2,
            FinaleWinnerFinal,
            GameBoardFinal,
            GameBoardRound0,
            GameBoardRound1,
            GameBoardRound2
        }

        /*
         * Constructor
         */
        
        public FormMediaSingle(MediaName mn)
        {
            // Initialize
            InitializeComponent();

            // Media player settings
            this.WindowsMediaPlayerMain.stretchToFit = true;
            this.WindowsMediaPlayerMain.uiMode = "none";

            // Load media
            this.LoadMedia(mn);
        }

        /*
         * Form Events
         */
        
        private void FormMediaSingle_FormClosing(object sender, FormClosingEventArgs e)
        {
            // Close media player
            this.WindowsMediaPlayerMain.close();
            this.WindowsMediaPlayerMain.Dispose();
        }

        private void FormMediaSingle_KeyDown(object sender, KeyEventArgs e)
        {
            // Get click event
            switch (e.KeyCode)
            {
                // Stop playback
                case Keys.Decimal:
                    // Stop
                    this.WindowsMediaPlayerMain.Ctlcontrols.currentPosition = Resources.MediaEndTime;

                    // Exit
                    break;

                // Other
                default:
                    // Exit
                    break;
            }
        }

        /*
         * Other Events
         */
        
        private void pictureBoxImage_Click(object sender, EventArgs e)
        {
            // Exit form
            this.Close();
        }

        private void WindowsMediaPlayerMain_PlayStateChange(object sender, AxWMPLib._WMPOCXEvents_PlayStateChangeEvent e)
        {
            // Check if the play state changed to "MediaEnded"
            if (e.newState == 8)
            {
                // Exit form
                this.Close();
            }
        }

        /*
         * Methods
         */
        
        private void LoadMedia(MediaName mn)
        {
            // Check media type
            switch (mn)
            {
                // Dynamic\Custom0
                case MediaName.DynamicCustom0:
                    // Check if file exists
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom0.mp4")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Dynamic\Custom0.mp4");
                    }

                    // Components
                    this.WindowsMediaPlayerMain.Visible = true;

                    // Play video
                    this.WindowsMediaPlayerMain.URL = Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom0.mp4");

                    // Exit
                    break;

                // Dynamic\Custom1
                case MediaName.DynamicCustom1:
                    // Check if file exists
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom1.mp4")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Dynamic\Custom1.mp4");
                    }

                    // Components
                    this.WindowsMediaPlayerMain.Visible = true;

                    // Play video
                    this.WindowsMediaPlayerMain.URL = Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom1.mp4");

                    // Exit
                    break;

                // Dynamic\Custom2
                case MediaName.DynamicCustom2:
                    // Check if file exists
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom2.mp4")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Dynamic\Custom2.mp4");
                    }

                    // Components
                    this.WindowsMediaPlayerMain.Visible = true;

                    // Play video
                    this.WindowsMediaPlayerMain.URL = Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom2.mp4");

                    // Exit
                    break;

                // Dynamic\Custom3
                case MediaName.DynamicCustom3:
                    // Check if file exists
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom3.mp4")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Dynamic\Custom3.mp4");
                    }

                    // Components
                    this.WindowsMediaPlayerMain.Visible = true;

                    // Play video
                    this.WindowsMediaPlayerMain.URL = Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom3.mp4");

                    // Exit
                    break;

                // Dynamic\Custom4
                case MediaName.DynamicCustom4:
                    // Check if file exists
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom4.mp4")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Dynamic\Custom4.mp4");
                    }

                    // Components
                    this.WindowsMediaPlayerMain.Visible = true;

                    // Play video
                    this.WindowsMediaPlayerMain.URL = Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom4.mp4");

                    // Exit
                    break;

                // Dynamic\Custom5
                case MediaName.DynamicCustom5:
                    // Check if file exists
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom5.mp4")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Dynamic\Custom5.mp4");
                    }

                    // Components
                    this.WindowsMediaPlayerMain.Visible = true;

                    // Play video
                    this.WindowsMediaPlayerMain.URL = Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom5.mp4");

                    // Exit
                    break;

                // Dynamic\Custom6
                case MediaName.DynamicCustom6:
                    // Check if file exists
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom6.mp4")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Dynamic\Custom6.mp4");
                    }

                    // Components
                    this.WindowsMediaPlayerMain.Visible = true;

                    // Play video
                    this.WindowsMediaPlayerMain.URL = Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom6.mp4");

                    // Exit
                    break;

                // Dynamic\Custom7
                case MediaName.DynamicCustom7:
                    // Check if file exists
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom7.mp4")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Dynamic\Custom7.mp4");
                    }

                    // Components
                    this.WindowsMediaPlayerMain.Visible = true;

                    // Play video
                    this.WindowsMediaPlayerMain.URL = Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom7.mp4");

                    // Exit
                    break;

                // Dynamic\Custom8
                case MediaName.DynamicCustom8:
                    // Check if file exists
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom8.mp4")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Dynamic\Custom8.mp4");
                    }

                    // Components
                    this.WindowsMediaPlayerMain.Visible = true;

                    // Play video
                    this.WindowsMediaPlayerMain.URL = Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom8.mp4");

                    // Exit
                    break;

                // Dynamic\Custom9
                case MediaName.DynamicCustom9:
                    // Check if file exists
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom9.mp4")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Dynamic\Custom9.mp4");
                    }

                    // Components
                    this.WindowsMediaPlayerMain.Visible = true;

                    // Play video
                    this.WindowsMediaPlayerMain.URL = Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom9.mp4");

                    // Exit
                    break;

                // Dynamic\Custom10
                case MediaName.DynamicCustom10:
                    // Check if file exists
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom10.mp4")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Dynamic\Custom10.mp4");
                    }

                    // Components
                    this.WindowsMediaPlayerMain.Visible = true;

                    // Play video
                    this.WindowsMediaPlayerMain.URL = Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom10.mp4");

                    // Exit
                    break;

                // Dynamic\Custom11
                case MediaName.DynamicCustom11:
                    // Check if file exists
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom11.mp4")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Dynamic\Custom11.mp4");
                    }

                    // Components
                    this.WindowsMediaPlayerMain.Visible = true;

                    // Play video
                    this.WindowsMediaPlayerMain.URL = Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom11.mp4");

                    // Exit
                    break;

                // Dynamic\Custom12
                case MediaName.DynamicCustom12:
                    // Check if file exists
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom12.mp4")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Dynamic\Custom12.mp4");
                    }

                    // Components
                    this.WindowsMediaPlayerMain.Visible = true;

                    // Play video
                    this.WindowsMediaPlayerMain.URL = Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom12.mp4");

                    // Exit
                    break;

                // Dynamic\Custom13
                case MediaName.DynamicCustom13:
                    // Check if file exists
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom13.mp4")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Dynamic\Custom13.mp4");
                    }

                    // Components
                    this.WindowsMediaPlayerMain.Visible = true;

                    // Play video
                    this.WindowsMediaPlayerMain.URL = Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom13.mp4");

                    // Exit
                    break;

                // Finale\Winner0
                case MediaName.FinaleWinner0:
                    // Check if file exists
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Finale\Winner0.mp4")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Finale\Winner0.mp4");
                    }

                    // Components
                    this.WindowsMediaPlayerMain.Visible = true;

                    // Play video
                    this.WindowsMediaPlayerMain.URL = Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Finale\Winner0.mp4");

                    // Exit
                    break;

                // Finale\Winner1
                case MediaName.FinaleWinner1:
                    // Check if file exists
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Finale\Winner1.mp4")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Finale\Winner1.mp4");
                    }

                    // Components
                    this.WindowsMediaPlayerMain.Visible = true;

                    // Play video
                    this.WindowsMediaPlayerMain.URL = Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Finale\Winner1.mp4");

                    // Exit
                    break;

                // Finale\Winner2
                case MediaName.FinaleWinner2:
                    // Check if file exists
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Finale\Winner2.mp4")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Finale\Winner2.mp4");
                    }

                    // Components
                    this.WindowsMediaPlayerMain.Visible = true;

                    // Play video
                    this.WindowsMediaPlayerMain.URL = Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Finale\Winner2.mp4");

                    // Exit
                    break;

                // Finale\WinnerFinal
                case MediaName.FinaleWinnerFinal:
                    // Check if file exists
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Finale\WinnerFinal.mp4")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Finale\WinnerFinal.mp4");
                    }

                    // Components
                    this.WindowsMediaPlayerMain.Visible = true;

                    // Play video
                    this.WindowsMediaPlayerMain.URL = Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Finale\WinnerFinal.mp4");

                    // Exit
                    break;

                // GameBoard\Final
                case MediaName.GameBoardFinal:
                    // Check if file exists
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"GameBoard\Final.png")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"GameBoard\Final.png");
                    }

                    // Components
                    this.pictureBoxImage.Enabled = true;
                    this.pictureBoxImage.Visible = true;

                    // Show image
                    this.pictureBoxImage.Image = Image.FromFile(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"GameBoard\Final.png"));

                    // Exit
                    break;

                // GameBoard\Round0
                case MediaName.GameBoardRound0:
                    // Check if file exists
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"GameBoard\Round0.png")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"GameBoard\Round0.png");
                    }

                    // Components
                    this.pictureBoxImage.Enabled = true;
                    this.pictureBoxImage.Visible = true;

                    // Show image
                    this.pictureBoxImage.Image = Image.FromFile(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"GameBoard\Round0.png"));

                    // Exit
                    break;

                // GameBoard\Round1
                case MediaName.GameBoardRound1:
                    // Check if file exists
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"GameBoard\Round1.png")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"GameBoard\Round1.png");
                    }

                    // Components
                    this.pictureBoxImage.Enabled = true;
                    this.pictureBoxImage.Visible = true;

                    // Show image
                    this.pictureBoxImage.Image = Image.FromFile(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"GameBoard\Round1.png"));

                    // Exit
                    break;

                // GameBoard\Round2
                case MediaName.GameBoardRound2:
                    // Check if file exists
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"GameBoard\Round2.png")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"GameBoard\Round2.png");
                    }

                    // Components
                    this.pictureBoxImage.Enabled = true;
                    this.pictureBoxImage.Visible = true;

                    // Show image
                    this.pictureBoxImage.Image = Image.FromFile(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"GameBoard\Round2.png"));

                    // Exit
                    break;

                // Other
                default:
                    // Exit
                    break;
            }
        }
    }
}
