﻿/********************************
 * Super Stop N Buy
 * AdminManagerAdd.cs
 * Created by Justin Leonard
 * < Other Names Omitted >
********************************/

using SuperStopNBuy.SuperStopNBuyClasses;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace SuperStopNBuy
{
    public partial class AdminManagerAdd : Form
    {
        ManagerClass aManager = new ManagerClass();

        public AdminManagerAdd()
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

        private void buttonSaveAndExit_Click(object sender, EventArgs e)
        {
            int tempVal = 0;

            // Check user name text box
            if (String.IsNullOrEmpty(textboxUsername.Text))
            {
                MessageBox.Show("Please enter a valid user name", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            // Check password text box
            if (String.IsNullOrEmpty(textboxPassword.Text))
            {
                MessageBox.Show("Please enter a valid password", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            // Check first name text box
            if (String.IsNullOrEmpty(textboxFirstName.Text))
            {
                MessageBox.Show("Please enter a valid first name", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            // Check last name text box
            if (String.IsNullOrEmpty(textboxLastName.Text))
            {
                MessageBox.Show("Please enter a valid last name", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            // Check access level combo box
            if (String.IsNullOrEmpty(comboBoxAccessLevel.Text))
            {
                MessageBox.Show("Please enter a valid access level", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            // Check if combo box is integer
            if (!Int32.TryParse(comboBoxAccessLevel.Text, out tempVal))
            {
                MessageBox.Show("Access level must be a number", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            aManager.managerUsername = textboxUsername.Text;
            aManager.managerPassword = textboxPassword.Text;
            aManager.managerFName = textboxFirstName.Text;
            aManager.managerLName = textboxLastName.Text;
            aManager.managerAccessLvl = Convert.ToInt32(comboBoxAccessLevel.Text);

            bool wasSuccessful = aManager.InsertToDatabase(aManager);
            if (wasSuccessful)
            {
                MessageBox.Show("Successful");
            }

            this.Hide();
            var formTemp = new AdminMain();
            formTemp.Show();
        }

        private void buttonBack_Click(object sender, EventArgs e)
        {
            this.Hide();
            var formTemp = new AdminMain();
            formTemp.Show();
        }
    }
}