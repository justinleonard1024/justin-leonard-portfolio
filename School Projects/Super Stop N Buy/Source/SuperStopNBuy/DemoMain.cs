﻿/********************************
 * Super Stop N Buy
 * DemoMain.cs
 * Created by Justin Leonard
 * < Other Names Omitted >
********************************/

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace SuperStopNBuy
{
    public partial class DemoMain : Form
    {
        public DemoMain()
        {
            InitializeComponent();
        }

        protected override void OnFormClosing(FormClosingEventArgs e)
        {
            // Initialize
            base.OnFormClosing(e);
            if (e.CloseReason == CloseReason.WindowsShutDown) return;

            // Exit
            Environment.Exit(Environment.ExitCode);
        }

        private void buttonManagement_Click(object sender, EventArgs e)
        {
            this.Hide();
            var formTemp = new ManagementLogin();
            formTemp.Show();
        }

        private void buttonStore_Click(object sender, EventArgs e)
        {
            this.Hide();
            var formTemp = new StoreMain();
            formTemp.Show();
        }
    }
}
