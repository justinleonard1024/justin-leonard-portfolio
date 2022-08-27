/********************************
 * Super Stop N Buy
 * ManagementItemView.cs
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
    public partial class ManagementItemView : Form
    {
        ItemClass anItem = new ItemClass();
        ItemClass selectedItem = new ItemClass();

        public ManagementItemView()
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

        private void buttonAdd_Click(object sender, EventArgs e)
        {
            this.Hide();
            var formTemp = new ManagementItemAdd();
            formTemp.Show();
        }

        private void ManagementItemView_Load(object sender, EventArgs e)
        {
            DataTable databaseTable = anItem.Select();
            dataGridItem.DataSource = databaseTable;
            dataGridItem.Columns[0].Width = 250;
        }

        public void dataGridItem_CellMouseClick(object sender, DataGridViewCellMouseEventArgs e)
        {
            int rowIndex = e.RowIndex;
            if (rowIndex >= 0)
            {
                selectedItem.itemName = dataGridItem.Rows[rowIndex].Cells[0].Value.ToString();
                selectedItem.itemNumber = Convert.ToInt32(dataGridItem.Rows[rowIndex].Cells[1].Value.ToString());
                selectedItem.itemPrice = Convert.ToDouble(dataGridItem.Rows[rowIndex].Cells[2].Value.ToString());
                selectedItem.itemCategory = dataGridItem.Rows[rowIndex].Cells[3].Value.ToString();
            }
        }

        public void buttonEdit_Click(object sender, EventArgs e)
        {
            try
            {
                
                var formTemp = new ManagementItemEdit(selectedItem);
                this.Hide();
                formTemp.Show();
            }
            catch
            {
                MessageBox.Show("Must Select A Value to Edit");
            }

        }

        private async void buttonDelete_Click(object sender, EventArgs e)
        {
            if (selectedItem != null)
            {
                DropboxTools dropboxTools = new DropboxTools();
                bool wasSuccessful = selectedItem.DeleteDatabaseItem(selectedItem);

                try
                {
                    await dropboxTools.Delete(Path.Combine(Global.AppDirectory, selectedItem.itemNumber + Global.AppExtension));
                }
                catch
                {
                    wasSuccessful = false;
                }

                if (wasSuccessful)
                {
                    MessageBox.Show("Item Successfully Deleted");
                }
                DataTable databaseTable = anItem.Select();
                dataGridItem.DataSource = databaseTable;
            }
            else
            {
                MessageBox.Show("Please Select an Item");
            }
        }

        private void buttonBack_Click(object sender, EventArgs e)
        {
            this.Hide();
            var formTemp = new ManagementLogin();
            formTemp.Show();
        }

        private void textboxSearch_Click(object sender, EventArgs e)
        {
            textboxSearch.Text = "";
        }

        private void buttonSearch_Click(object sender, EventArgs e)
        {
            DataTable databaseTable = anItem.SelectSearch(textboxSearch.Text, true);
            dataGridItem.DataSource = databaseTable;
        }

        private void dataGridItem_DataSourceChanged(object sender, EventArgs e)
        {
            if (dataGridItem.Rows.Count != 0)
            {
                dataGridItem.Rows[0].Selected = true;
            }
        }
    }
}
