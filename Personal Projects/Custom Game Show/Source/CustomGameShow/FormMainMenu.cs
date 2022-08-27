/********************************
 * Custom Game Show
 * FormMainMenu.cs
 * Created by Justin Leonard
********************************/

using System;
using System.Windows.Forms;

namespace CustomGameShow
{
    public partial class FormMainMenu : Form
    {
        /*
         * Fields
         */
        Timer timerFade;

        /*
         * Constructor
         */
        
        public FormMainMenu()
        {
            // Initialize
            InitializeComponent();
        }

        /*
         * Form Events
         */
        
        private void FormMainMenu_Load(object sender, EventArgs e)
        {
            // Fade in
            this.FadeForm();
        }

        /*
         * Button Events
         */
        
        private void buttonStartGame_Click(object sender, EventArgs e)
        {
            // Start the game
            this.StartGame();
        }

        private void buttonSettings_Click(object sender, EventArgs e)
        {
            // Display Settings
            this.DisplaySettings();
        }

        private void buttonLog_Click(object sender, EventArgs e)
        {
            // Display Log
            this.DisplayLog();
        }

        private void buttonExit_Click(object sender, EventArgs e)
        {
            // Exit application
            Application.Exit();
        }

        /*
         * Methods
         */
        
        private void StartGame()
        {
            // Disable main menu
            this.Enabled = false;

            // Don't show in taskbar
            this.ShowInTaskbar = false;
            
            // Variables
            Form tempForm = new FormGameBoard();

            // Show form
            var result = tempForm.ShowDialog();
        }

        private void DisplaySettings()
        {
            // Variables
            Form tempForm = new FormMainSettings();

            // Show form
            var result = tempForm.ShowDialog();
        }

        private void DisplayLog()
        {
            // Variables
            Form tempForm = new FormMainLog();

            // Show form
            var result = tempForm.ShowDialog();
        }

        private void FadeForm()
        {
            // Variables
            timerFade = new Timer();

            // Timer settings
            timerFade.Interval = 15;

            // Fade in
            timerFade.Tick += new EventHandler(FadeIn);
            timerFade.Start();
        }

        private void FadeIn(object sender, EventArgs e)
        {
            // Fade in
            if (this.Opacity >= 1)
            {
                // Stop timer
                this.timerFade.Stop();

                // Enable Form
                this.Enabled = true;

                // Focus form
                this.Focus();
            }
            else
            {
                // Increase opacity
                this.Opacity += 0.01;
            }
        }
    }
}
