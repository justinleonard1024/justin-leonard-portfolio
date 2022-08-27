/********************************
 * Custom Game Show
 * FormMediaInitial.cs
 * Created by Justin Leonard
********************************/

using System;
using System.IO;
using System.Windows.Forms;

namespace CustomGameShow
{
    public partial class FormMediaInitial : Form
    {
        /*
         * Constructor
         */
        
        public FormMediaInitial()
        {
            // Initialize
            InitializeComponent();

            // Media player settings
            this.WindowsMediaPlayerMain.stretchToFit = true;
            this.WindowsMediaPlayerMain.uiMode = "none";
        }

        /*
         * Form Events
         */
        
        private void FormMediaInitial_Load(object sender, EventArgs e)
        {
            // Load media
            this.LoadMedia();
        }

        private void FormMediaInitial_FormClosing(object sender, FormClosingEventArgs e)
        {
            // Close media player
            this.WindowsMediaPlayerMain.close();
            this.WindowsMediaPlayerMain.Dispose();
        }

        private void FormMediaInitial_KeyDown(object sender, KeyEventArgs e)
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
        
        private void WindowsMediaPlayerMain_PlayStateChange(object sender, AxWMPLib._WMPOCXEvents_PlayStateChangeEvent e)
        {
            // Check if the play state changed to "MediaEnded"
            if (e.newState == 8)
            {
                // Close form
                this.Close();
            }
        }

        /*
         * Methods
         */
        
        public void LoadMedia()
        {
            // Check if file exists
            if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"GameBoard\Initial.mp4")))
            {
                // Error
                Resources.Error(Resources.ErrorCode.MissingMedia, @"GameBoard\Initial.mp4");
            }

            // Play video
            this.WindowsMediaPlayerMain.URL = Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"GameBoard\Initial.mp4");
        }
    }
}
