/********************************
 * Super Stop N Buy
 * ManagementItemEdit.cs
 * Created by Justin Leonard
 * < Other Names Omitted >
********************************/

using SuperStopNBuy.SuperStopNBuyClasses;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace SuperStopNBuy
{
    public partial class ManagementItemEdit : Form
    {
        ItemClass anItem = new ItemClass();

        public ManagementItemEdit()
        {
            InitializeComponent();
        }

        protected override void OnFormClosing(FormClosingEventArgs e)
        {
            // Initialize
            base.OnFormClosing(e);
            if (e.CloseReason == CloseReason.WindowsShutDown) return;

            // Open form
            this.Hide();
            DemoMain formDemoMain = new DemoMain();
            formDemoMain.Show();
        }

        public ManagementItemEdit(ItemClass item)
        {
            InitializeComponent();

            anItem = item;

            textboxName.Text = anItem.itemName;
            textboxPrice.Text = anItem.itemPrice.ToString();
            textboxNumber.Text = anItem.itemNumber.ToString();
            comboBoxCategory.Text = anItem.itemCategory.ToString();

        }

        private async void buttonSubmit_Click(object sender, EventArgs e)
        {
            // Check name text box
            if (String.IsNullOrEmpty(textboxName.Text))
            {
                MessageBox.Show("Please enter a valid product name", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            // Check price text box
            if (String.IsNullOrEmpty(textboxPrice.Text))
            {
                MessageBox.Show("Please enter a valid product price", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            // Check number text box
            if (String.IsNullOrEmpty(textboxNumber.Text) || textboxNumber.Text.Length != textboxNumber.MaxLength)
            {
                MessageBox.Show("Please enter a valid product number", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            // Check category combo box
            if (String.IsNullOrEmpty(comboBoxCategory.Text))
            {
                MessageBox.Show("Please enter a valid product category", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            // Check picture box
            if (pictureBoxImport.Image == null)
            {
                MessageBox.Show("Please select an image", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            DropboxTools dropboxTools = new DropboxTools();

            anItem.itemName = textboxName.Text;
            anItem.itemNumber = Convert.ToInt32(textboxNumber.Text);
            anItem.itemPrice = Convert.ToDouble(textboxPrice.Text);
            anItem.itemCategory = comboBoxCategory.Text;

            bool wasSuccessful = anItem.UpdateDatabaseItem(anItem);

            try
            {
                this.Enabled = false;
                await dropboxTools.Upload(openFileDialogImport.FileName, Path.Combine(Global.AppDirectory, textboxNumber.Text + Global.AppExtension));
            }
            catch
            {
                wasSuccessful = false;
            }

            if (wasSuccessful)
            {
                MessageBox.Show("Update Successful");
            }
            else
            {
                MessageBox.Show("Update Not Successful");
            }

            this.Hide();
            var formTemp = new ManagementItemView();
            formTemp.Show();
        }

        private void buttonBack_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Changes will not be saved");
            this.Hide();
            var formTemp = new ManagementItemView();
            formTemp.Show();
        }

        private void buttonImport_Click(object sender, EventArgs e)
        {
            if (openFileDialogImport.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                // Variables
                Image importPicture;

                // Get picture
                importPicture = Image.FromFile(openFileDialogImport.FileName);

                // Check picture size
                if (importPicture.Height != 150 || importPicture.Width != 150)
                {
                    // Clear data
                    pictureBoxImport.Image = null;
                    openFileDialogImport.FileName = String.Empty;

                    // Error
                    MessageBox.Show("Image size must be exactly 150 x 150", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
                else
                {
                    // Set picture box to selected picture
                    pictureBoxImport.Image = importPicture;
                }
            }
        }

        private async void ManagementItemEdit_Load(object sender, EventArgs e)
        {
            string srcFileName, trgFileName;
            DropboxTools dropboxTools = new DropboxTools();

            srcFileName = Global.AppDirectory + anItem.itemNumber + Global.AppExtension;
            trgFileName = Global.GetTemporaryDownloadPath() + anItem.itemNumber + Global.AppExtension;

            try
            {
                await dropboxTools.DownloadToPictureBox(srcFileName, trgFileName, pictureBoxImport);
            }
            catch
            {
                // Error
            }
        }
    }
}
