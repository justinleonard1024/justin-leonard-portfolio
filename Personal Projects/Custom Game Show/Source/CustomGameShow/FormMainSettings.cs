/********************************
 * Custom Game Show
 * FormMainSettings.cs
 * Created by Justin Leonard
********************************/

using System;
using System.Configuration;
using System.Drawing;
using System.Windows.Forms;

namespace CustomGameShow
{
    public partial class FormMainSettings : Form
    {
        /*
         * Fields
         */
        string[] settingsKeys, settingsValues;

        /*
         * Constructor
         */
        
        public FormMainSettings()
        {
            // Initialize
            InitializeComponent();

            // Variables
            var settings = ConfigurationManager.AppSettings;

            // Set fields
            this.settingsKeys = settings.AllKeys;
            this.settingsValues = new string[this.settingsKeys.Length];
            for (int i = 0; i < this.settingsKeys.Length; i++)
            {
                this.settingsValues[i] = settings[settingsKeys[i]];
            }
        }

        /*
         * Form Events
         */
        
        private void FormMainSettings_Load(object sender, EventArgs e)
        {
            // Select index
            listBoxText.SelectedIndex = 0;
            listBoxColor.SelectedIndex = 0;
            listBoxType.SelectedIndex = 0;
        }

        /*
         * Other Events
         */
        
        private void listBoxText_SelectedIndexChanged(object sender, EventArgs e)
        {
            // Set text
            textBoxText.Text = this.settingsValues[listBoxText.SelectedIndex];
        }

        private void listBoxColor_SelectedIndexChanged(object sender, EventArgs e)
        {
            // Variables
            string[] tempColor;

            // Get color
            tempColor = this.settingsValues[listBoxColor.SelectedIndex + Resources.SettingsOffsetColor].Split(' ');

            // Set colors
            try
            {
                pictureBoxColor.BackColor = Color.FromArgb(Int32.Parse(tempColor[0]), Int32.Parse(tempColor[1]), Int32.Parse(tempColor[2]));
                colorDialogMain.Color = Color.FromArgb(Int32.Parse(tempColor[0]), Int32.Parse(tempColor[1]), Int32.Parse(tempColor[2]));
            }
            catch
            {
                // Error
                Resources.Error(Resources.ErrorCode.InvalidContestantColor, this.settingsValues[listBoxColor.SelectedIndex + Resources.SettingsOffsetColor]);
            }
        }

        private void listBoxType_SelectedIndexChanged(object sender, EventArgs e)
        {
            // Set combo box
            switch (this.settingsValues[listBoxType.SelectedIndex + Resources.SettingsOffsetMediaType])
            {
                // Image question followed by an image answer
                case "ImageImage":
                    // Set box
                    comboBoxType.SelectedIndex = 0;

                    // Exit
                    break;

                // Image prompt and a video question followed by an image question and an image answer
                case "ImageVideoImageImage":
                    // Set box
                    comboBoxType.SelectedIndex = 1;

                    // Exit
                    break;

                // Image prompt and a video question followed by an image question and a video answer
                case "ImageVideoImageVideo":
                    // Set box
                    comboBoxType.SelectedIndex = 2;

                    // Exit
                    break;

                // Video question followed by an image question and an image answer
                case "VideoImageImage":
                    // Set box
                    comboBoxType.SelectedIndex = 3;

                    // Exit
                    break;

                // Video question followed by an image question and a video answer
                case "VideoImageVideo":
                    // Set box
                    comboBoxType.SelectedIndex = 4;

                    // Exit
                    break;

                // Other
                default:
                    // Exit
                    break;
            }
        }

        /*
         * Button Events
         */
        
        private void buttonColor_Click(object sender, EventArgs e)
        {
            // Select color
            if (colorDialogMain.ShowDialog() == DialogResult.OK)
            {
                // Change picture box color
                pictureBoxColor.BackColor = colorDialogMain.Color;
            }
        }

        private void buttonSaveText_Click(object sender, EventArgs e)
        {
            // Check text box
            if (!String.IsNullOrEmpty(textBoxText.Text))
            {
                // Set value
                this.settingsValues[listBoxText.SelectedIndex] = textBoxText.Text;
            }
            else
            {
                // Error message
                MessageBox.Show("The text box is empty", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void buttonSaveColor_Click(object sender, EventArgs e)
        {
            // Set value
            this.settingsValues[listBoxColor.SelectedIndex + Resources.SettingsOffsetColor] = colorDialogMain.Color.R.ToString() + " " + colorDialogMain.Color.G.ToString() + " " + colorDialogMain.Color.B.ToString();
        }

        private void buttonSaveType_Click(object sender, EventArgs e)
        {
            // Set value
            this.settingsValues[listBoxType.SelectedIndex + Resources.SettingsOffsetMediaType] = comboBoxType.SelectedItem.ToString();
        }

        private void buttonSaveAll_Click(object sender, EventArgs e)
        {
            // Variables
            Configuration config;
            DialogResult result;

            // Open message box
            result = MessageBox.Show("Are you sure you want to save all settings? It will require the application to restart immediately.", "Settings", MessageBoxButtons.YesNo, MessageBoxIcon.Question);

            // Check result
            if (result == DialogResult.Yes)
            {
                // Open manager
                config = ConfigurationManager.OpenExeConfiguration(ConfigurationUserLevel.None);

                // Set values
                for (int i = 0; i < this.settingsKeys.Length; i++)
                {
                    config.AppSettings.Settings[this.settingsKeys[i]].Value = this.settingsValues[i];
                }

                // Save configuration
                config.Save(ConfigurationSaveMode.Full, true);
                ConfigurationManager.RefreshSection("appSettings");

                // Exit application
                Application.Exit();
            }
        }

        private void buttonExit_Click(object sender, EventArgs e)
        {
            // Exit form
            this.Close();
        }
    }
}
