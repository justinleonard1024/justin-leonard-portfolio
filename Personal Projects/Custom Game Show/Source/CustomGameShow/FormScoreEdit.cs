/********************************
 * Custom Game Show
 * FormScoreEdit.cs
 * Created by Justin Leonard
********************************/

using System;
using System.Configuration;
using System.Drawing;
using System.Windows.Forms;

namespace CustomGameShow
{
    public partial class FormScoreEdit : Form
    {
        /*
         * Fields
         */
        FormGameBoard mainForm;

        /*
         * Constructor
         */
        
        public FormScoreEdit(FormGameBoard fgb)
        {
            // Initialize
            InitializeComponent();

            // Set fields
            mainForm = fgb;
        }

        /*
         * Form Events
         */
        
        private void FormScoreEdit_Load(object sender, EventArgs e)
        {
            // Set display
            this.SetDisplay();
        }

        private void FormScoreEdit_KeyDown(object sender, KeyEventArgs e)
        {
            // Get click event
            switch (e.KeyCode)
            {
                // Custom 0
                case Keys.NumPad0:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom0);

                    // Exit
                    break;

                // Custom 1
                case Keys.NumPad1:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom1);

                    // Exit
                    break;

                // Custom 2
                case Keys.NumPad2:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom2);

                    // Exit
                    break;

                // Custom 3
                case Keys.NumPad3:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom3);

                    // Exit
                    break;

                // Custom 4
                case Keys.NumPad4:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom4);

                    // Exit
                    break;

                // Custom 5
                case Keys.NumPad5:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom5);

                    // Exit
                    break;

                // Custom 6
                case Keys.NumPad6:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom6);

                    // Exit
                    break;

                // Custom 7
                case Keys.NumPad7:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom7);

                    // Exit
                    break;

                // Custom 8
                case Keys.NumPad8:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom8);

                    // Exit
                    break;

                // Custom 9
                case Keys.NumPad9:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom9);

                    // Exit
                    break;

                // Custom 10
                case Keys.Divide:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom10);

                    // Exit
                    break;

                // Custom 11
                case Keys.Multiply:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom11);

                    // Exit
                    break;

                // Custom 12
                case Keys.Subtract:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom12);

                    // Exit
                    break;

                // Custom 13
                case Keys.Add:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom13);

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
        
        private void comboBoxContestant_SelectedIndexChanged(object sender, EventArgs e)
        {
            // Get contestant
            switch (this.comboBoxContestant.SelectedIndex)
            {
                // Contestant 0
                case 0:
                    // Set numeric
                    this.numericUpDownScore.Value = mainForm.score0;

                    // Exit
                    break;

                // Contestant 1
                case 1:
                    // Set numeric
                    this.numericUpDownScore.Value = mainForm.score1;

                    // Exit
                    break;

                // Contestant 2
                case 2:
                    // Set numeric
                    this.numericUpDownScore.Value = mainForm.score2;

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
        
        private void buttonSaveScore_Click(object sender, EventArgs e)
        {
            // Variables
            var settings = ConfigurationManager.AppSettings;

            // Get contestant
            switch (this.comboBoxContestant.SelectedIndex)
            {
                // Contestant 0
                case 0:
                    // Set values
                    labelScore0.Text = settings["contestantName0"] + ": " + Convert.ToInt32(this.numericUpDownScore.Value);
                    this.mainForm.score0 = Convert.ToInt32(this.numericUpDownScore.Value);

                    // Update log
                    this.mainForm.UpdateLog();

                    // Exit
                    break;

                // Contestant 1
                case 1:
                    // Set values
                    labelScore1.Text = settings["contestantName1"] + ": " + Convert.ToInt32(this.numericUpDownScore.Value);
                    this.mainForm.score1 = Convert.ToInt32(this.numericUpDownScore.Value);

                    // Update log
                    this.mainForm.UpdateLog();

                    // Exit
                    break;

                // Contestant 2
                case 2:
                    // Set values
                    labelScore2.Text = settings["contestantName2"] + ": " + Convert.ToInt32(this.numericUpDownScore.Value);
                    this.mainForm.score2 = Convert.ToInt32(this.numericUpDownScore.Value);

                    // Update log
                    this.mainForm.UpdateLog();

                    // Exit
                    break;

                // Other
                default:
                    // Exit
                    break;
            }
        }

        private void buttonExit_Click(object sender, EventArgs e)
        {
            // Exit form
            this.Close();
        }

        /*
         * Methods
         */
        
        private void SetDisplay()
        {
            // Variables
            int s0, s1, s2;
            string[] tempColor = new string[1];
            var settings = ConfigurationManager.AppSettings;

            // Set values
            s0 = mainForm.score0;
            s1 = mainForm.score1;
            s2 = mainForm.score2;

            // Set labels
            labelScore0.Text = settings["contestantName0"] + ": " + s0.ToString();
            labelScore1.Text = settings["contestantName1"] + ": " + s1.ToString();
            labelScore2.Text = settings["contestantName2"] + ": " + s2.ToString();

            // Set color
            tempColor = settings["contestantColor0"].Split(' ');
            labelScore0.ForeColor = Color.FromArgb(Int32.Parse(tempColor[0]), Int32.Parse(tempColor[1]), Int32.Parse(tempColor[2]));

            tempColor = settings["contestantColor1"].Split(' ');
            labelScore1.ForeColor = Color.FromArgb(Int32.Parse(tempColor[0]), Int32.Parse(tempColor[1]), Int32.Parse(tempColor[2]));

            tempColor = settings["contestantColor2"].Split(' ');
            labelScore2.ForeColor = Color.FromArgb(Int32.Parse(tempColor[0]), Int32.Parse(tempColor[1]), Int32.Parse(tempColor[2]));

            // Set combo box
            this.comboBoxContestant.Items.AddRange(new object[] {
                settings["contestantName0"],
                settings["contestantName1"],
                settings["contestantName2"]});
            this.comboBoxContestant.SelectedIndex = 0;

            // Set numeric
            this.numericUpDownScore.Value = mainForm.score0;
        }

        private void DisplaySingle(FormMediaSingle.MediaName mn)
        {
            // Variables
            Form tempForm = new FormMediaSingle(mn);

            // Show form
            var result = tempForm.ShowDialog();
        }
    }
}
