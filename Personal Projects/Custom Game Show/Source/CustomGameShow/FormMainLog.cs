/********************************
 * Custom Game Show
 * FormMainLog.cs
 * Created by Justin Leonard
********************************/

using System;
using System.Configuration;
using System.Drawing;
using System.IO;
using System.Windows.Forms;

namespace CustomGameShow
{
    public partial class FormMainLog : Form
    {
        /*
         * Constructor
         */
        
        public FormMainLog()
        {
            // Initialize
            InitializeComponent();

            // Load media
            this.LoadMedia();
        }

        /*
         * Button Events
         */
        
        private void buttonExit_Click(object sender, EventArgs e)
        {
            // Exit form
            this.Close();
        }

        /*
         * Methods
         */
        
        private void LoadMedia()
        {
            // Variables
            Configuration config;

            // Open manager
            config = ConfigurationManager.OpenExeConfiguration(ConfigurationUserLevel.None);

            // Get value
            this.textBoxLog.Text = config.AppSettings.Settings["gameplayLog"].Value;

            // Save configuration
            config.Save(ConfigurationSaveMode.Full, true);
            ConfigurationManager.RefreshSection("appSettings");
        }
    }
}
